# Copyright (C) 2017-2024  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

import logging
from os import path
import re
import subprocess
from typing import Any, Dict, Iterator, List, Mapping, Optional, Sequence, Tuple

import attr
from dateutil.parser import parse as parse_date
from debian.changelog import Changelog
from debian.deb822 import Dsc
from looseversion import LooseVersion2

from swh.loader.core.utils import download, release_name
from swh.loader.package.loader import BasePackageInfo, PackageLoader, PartialExtID
from swh.model.hashutil import hash_to_bytes
from swh.model.model import ObjectType, Person, Release, Sha1Git, TimestampWithTimezone
from swh.storage.interface import StorageInterface

logger = logging.getLogger(__name__)
UPLOADERS_SPLIT = re.compile(r"(?<=\>)\s*,\s*")

EXTID_TYPE = "dsc-sha256"
EXTID_VERSION = 1


class DscCountError(ValueError):
    """Raised when an unexpected number of .dsc files is seen"""

    pass


@attr.s
class DebianFileMetadata:
    name = attr.ib(type=str)
    """Filename"""

    size = attr.ib(type=int)
    uri = attr.ib(type=str)
    """URL of this specific file"""

    # all checksums are not always available, make them optional
    sha256 = attr.ib(type=str, default="")
    md5sum = attr.ib(type=str, default="")
    sha1 = attr.ib(type=str, default="")

    # Some of the DSC files imported in swh apparently had a Checksums-SHA512
    # field which got recorded in the archive. Current versions of dpkg-source
    # don't seem to generate them, but keep the field available for
    # future-proofing.
    sha512 = attr.ib(type=str, default="")


@attr.s
class DebianPackageChangelog:
    person = attr.ib(type=Dict[str, str])
    """A dict with fields like, model.Person, except they are str instead
    of bytes, and 'email' is optional."""
    date = attr.ib(type=str)
    """Date of the changelog entry."""
    history = attr.ib(type=List[Tuple[str, str]])
    """List of tuples (package_name, version)"""


@attr.s
class DebianPackageInfo(BasePackageInfo):
    raw_info = attr.ib(type=Dict[str, Any])
    files = attr.ib(type=Dict[str, DebianFileMetadata])
    """Metadata of the files (.deb, .dsc, ...) of the package."""
    name = attr.ib(type=str)
    intrinsic_version = attr.ib(type=str)
    """eg. ``0.7.2-3``, while :attr:`version` would be ``stretch/contrib/0.7.2-3``"""

    @classmethod
    def from_metadata(
        cls, a_metadata: Dict[str, Any], url: str, version: str
    ) -> "DebianPackageInfo":
        intrinsic_version = a_metadata["version"]
        assert "/" in version and "/" not in intrinsic_version, (
            version,
            intrinsic_version,
        )
        return cls(
            url=url,
            filename=None,
            version=version,
            raw_info=a_metadata,
            files={
                file_name: DebianFileMetadata(**file_metadata)
                for (file_name, file_metadata) in a_metadata.get("files", {}).items()
            },
            name=a_metadata["name"],
            intrinsic_version=intrinsic_version,
        )

    def extid(self) -> Optional[PartialExtID]:
        dsc_files = [
            file for (name, file) in self.files.items() if name.endswith(".dsc")
        ]

        if len(dsc_files) != 1:
            raise DscCountError(
                f"Expected exactly one .dsc file for package {self.name}, "
                f"got {len(dsc_files)}"
            )

        return (
            EXTID_TYPE,
            EXTID_VERSION,
            hash_to_bytes(
                dsc_files[0].sha256 or dsc_files[0].sha1 or dsc_files[0].md5sum
            ),
        )


@attr.s
class IntrinsicPackageMetadata:
    """Metadata extracted from a package's .dsc file."""

    name = attr.ib(type=str)
    version = attr.ib(type=str)
    changelog = attr.ib(type=DebianPackageChangelog)
    maintainers = attr.ib(type=List[Dict[str, str]])
    """A list of dicts with fields like, model.Person, except they are str instead
    of bytes, and 'email' is optional."""


class DebianLoader(PackageLoader[DebianPackageInfo]):
    """Load debian origins into swh archive."""

    visit_type = "deb"

    def __init__(
        self,
        storage: StorageInterface,
        url: str,
        packages: Mapping[str, Any],
        **kwargs: Any,
    ):
        """Debian Loader implementation.

        Args:
            url: Origin url (e.g. deb://Debian/packages/cicero)
            date: Ignored
            packages: versioned packages and associated artifacts, example::

              {
                'stretch/contrib/0.7.2-3': {
                  'name': 'cicero',
                  'version': '0.7.2-3'
                  'files': {
                    'cicero_0.7.2-3.diff.gz': {
                       'md5sum': 'a93661b6a48db48d59ba7d26796fc9ce',
                       'name': 'cicero_0.7.2-3.diff.gz',
                       'sha256': 'f039c9642fe15c75bed5254315e2a29f...',
                       'size': 3964,
                       'uri': 'http://d.d.o/cicero_0.7.2-3.diff.gz',
                    },
                    'cicero_0.7.2-3.dsc': {
                      'md5sum': 'd5dac83eb9cfc9bb52a15eb618b4670a',
                      'name': 'cicero_0.7.2-3.dsc',
                      'sha256': '35b7f1048010c67adfd8d70e4961aefb...',
                      'size': 1864,
                      'uri': 'http://d.d.o/cicero_0.7.2-3.dsc',
                    },
                    'cicero_0.7.2.orig.tar.gz': {
                      'md5sum': '4353dede07c5728319ba7f5595a7230a',
                      'name': 'cicero_0.7.2.orig.tar.gz',
                      'sha256': '63f40f2436ea9f67b44e2d4bd669dbab...',
                      'size': 96527,
                      'uri': 'http://d.d.o/cicero_0.7.2.orig.tar.gz',
                    }
                  },
                },
                # ...
              }

        """
        super().__init__(storage=storage, url=url, **kwargs)
        self.packages = packages

    def get_sorted_versions(self) -> Sequence[str]:
        """Returns the keys of the packages input (e.g.
        stretch/contrib/0.7.2-3, etc...)

        """
        return list(
            sorted(
                self.packages, key=lambda p: LooseVersion2(self.packages[p]["version"])
            )
        )

    def get_package_info(self, version: str) -> Iterator[Tuple[str, DebianPackageInfo]]:
        meta = self.packages[version]
        p_info = DebianPackageInfo.from_metadata(
            meta, url=self.origin.url, version=version
        )
        yield release_name(version), p_info

    def download_package(
        self, p_info: DebianPackageInfo, tmpdir: str
    ) -> List[Tuple[str, Mapping]]:
        """Contrary to other package loaders (1 package, 1 artifact),
        `p_info.files` represents the package's datafiles set to fetch:
        - <package-version>.orig.tar.gz
        - <package-version>.dsc
        - <package-version>.diff.gz

        This is delegated to the `download_package` function.

        """
        all_hashes = download_package(p_info, tmpdir)
        logger.debug("all_hashes: %s", all_hashes)
        res = []
        for hashes in all_hashes.values():
            res.append((tmpdir, hashes))
            logger.debug("res: %s", res)
        return res

    def uncompress(
        self, dl_artifacts: List[Tuple[str, Mapping[str, Any]]], dest: str
    ) -> str:
        logger.debug("dl_artifacts: %s", dl_artifacts)
        return extract_package(dl_artifacts, dest=dest)

    def build_release(
        self,
        p_info: DebianPackageInfo,
        uncompressed_path: str,
        directory: Sha1Git,
    ) -> Optional[Release]:
        dsc_url, dsc_name = dsc_information(p_info)
        if not dsc_name:
            raise ValueError("dsc name for url %s should not be None" % dsc_url)
        dsc_path = path.join(path.dirname(uncompressed_path), dsc_name)
        intrinsic_metadata = get_intrinsic_package_metadata(
            p_info, dsc_path, uncompressed_path
        )

        logger.debug("intrinsic_metadata: %s", intrinsic_metadata)
        logger.debug("p_info: %s", p_info)

        msg = (
            f"Synthetic release for Debian source package {p_info.name} "
            f"version {p_info.intrinsic_version}\n"
        )

        author = prepare_person(intrinsic_metadata.changelog.person)
        date = TimestampWithTimezone.from_iso8601(intrinsic_metadata.changelog.date)

        # inspired from swh.loader.debian.converters.package_metadata_to_revision
        return Release(
            name=p_info.intrinsic_version.encode(),
            message=msg.encode(),
            author=author,
            date=date,
            target=directory,
            target_type=ObjectType.DIRECTORY,
            synthetic=True,
        )


def uid_to_person(uid: str) -> Dict[str, str]:
    """Convert an uid to a person suitable for insertion.

    Args:
        uid: an uid of the form "Name <email@address>"

    Returns:
        a dictionary with the following keys:

        - name: the name associated to the uid
        - email: the mail associated to the uid
        - fullname: the actual uid input

    """
    person = Person.from_fullname(uid.encode("utf-8"))
    return {k: v.decode("utf-8") for k, v in person.to_dict().items() if v is not None}


def prepare_person(person: Mapping[str, str]) -> Person:
    """Prepare person for swh serialization...

    Args:
        A person dict

    Returns:
        A person ready for storage

    """
    return Person.from_dict(
        {key: value.encode("utf-8") for (key, value) in person.items()}
    )


def download_package(p_info: DebianPackageInfo, tmpdir: Any) -> Mapping[str, Any]:
    """Fetch a source package in a temporary directory and check the checksums
    for all files.

    Args:
        p_info: Information on a package
        tmpdir: Where to download and extract the files to ingest

    Returns:
        Dict of swh hashes per filename key

    """
    all_hashes = {}
    for filename, fileinfo in p_info.files.items():
        uri = fileinfo.uri
        logger.debug("fileinfo: %s", fileinfo)
        extrinsic_hashes = {}
        if fileinfo.md5sum:
            extrinsic_hashes["md5"] = fileinfo.md5sum
        if fileinfo.sha256:
            extrinsic_hashes["sha256"] = fileinfo.sha256
        if fileinfo.sha1:
            extrinsic_hashes["sha1"] = fileinfo.sha1
        logger.debug("extrinsic_hashes(%s): %s", filename, extrinsic_hashes)
        _, hashes = download(
            uri, dest=tmpdir, filename=filename, hashes=extrinsic_hashes
        )
        all_hashes[filename] = hashes

    logger.debug("all_hashes: %s", all_hashes)
    return all_hashes


def dsc_information(p_info: DebianPackageInfo) -> Tuple[Optional[str], Optional[str]]:
    """Retrieve dsc information from a package.

    Args:
        p_info: Package metadata information

    Returns:
        Tuple of dsc file's uri, dsc's full disk path

    """
    dsc_name = None
    dsc_url = None
    for filename, fileinfo in p_info.files.items():
        if filename.endswith(".dsc"):
            if dsc_name:
                raise DscCountError(
                    "Package %s_%s references several dsc files."
                    % (p_info.name, p_info.intrinsic_version)
                )
            dsc_url = fileinfo.uri
            dsc_name = filename

    return dsc_url, dsc_name


def extract_package(dl_artifacts: List[Tuple[str, Mapping]], dest: str) -> str:
    """Extract a Debian source package to a given directory.

    Note that after extraction the target directory will be the root of the
    extracted package, rather than containing it.

    Args:
        package: package information dictionary
        dest: directory where the package files are stored

    Returns:
        Package extraction directory

    """
    a_path = dl_artifacts[0][0]
    logger.debug("dl_artifacts: %s", dl_artifacts)
    for _, hashes in dl_artifacts:
        logger.debug("hashes: %s", hashes)
        filename = hashes["filename"]
        if filename.endswith(".dsc"):
            dsc_name = filename
            break

    dsc_path = path.join(a_path, dsc_name)
    destdir = path.join(dest, "extracted")
    logfile = path.join(dest, "extract.log")
    logger.debug(
        "extract Debian source package %s in %s" % (dsc_path, destdir),
        extra={
            "swh_type": "deb_extract",
            "swh_dsc": dsc_path,
            "swh_destdir": destdir,
        },
    )

    cmd = [
        "dpkg-source",
        "--no-copy",
        "--no-check",
        "--ignore-bad-version",
        "-x",
        dsc_path,
        destdir,
    ]

    try:
        with open(logfile, "w") as stdout:
            subprocess.check_call(cmd, stdout=stdout, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        logdata = open(logfile, "r").read()
        raise ValueError(
            "dpkg-source exited with code %s: %s" % (e.returncode, logdata)
        ) from None

    return destdir


def get_intrinsic_package_metadata(
    p_info: DebianPackageInfo, dsc_path: str, extracted_path: str
) -> IntrinsicPackageMetadata:
    """Get the package metadata from the source package at dsc_path,
    extracted in extracted_path.

    Args:
        p_info: the package information
        dsc_path: path to the package's dsc file
        extracted_path: the path where the package got extracted

    Returns:
        dict: a dictionary with the following keys:

        - history: list of (package_name, package_version) tuples parsed from
          the package changelog

    """
    with open(dsc_path, "rb") as dsc:
        parsed_dsc = Dsc(dsc)

    # Parse the changelog to retrieve the rest of the package information
    changelog_path = path.join(extracted_path, "debian/changelog")
    with open(changelog_path, "rb") as changelog_file:
        try:
            parsed_changelog = Changelog(changelog_file)
        except UnicodeDecodeError:
            logger.warning(
                "Unknown encoding for changelog %s,"
                " falling back to iso" % changelog_path,
                extra={
                    "swh_type": "deb_changelog_encoding",
                    "swh_name": p_info.name,
                    "swh_version": str(p_info.version),
                    "swh_changelog": changelog_path,
                },
            )

            # need to reset as Changelog scrolls to the end of the file
            changelog_file.seek(0)
            parsed_changelog = Changelog(changelog_file, encoding="iso-8859-15")

    history: List[Tuple[str, str]] = []

    for block in parsed_changelog:
        assert block.package is not None and block._raw_version is not None
        history.append((block.package, block._raw_version))

    changelog = DebianPackageChangelog(
        person=uid_to_person(parsed_changelog.author),
        date=parse_date(parsed_changelog.date).isoformat(),
        history=history[1:],
    )

    maintainers = [
        uid_to_person(parsed_dsc["Maintainer"]),
    ]
    maintainers.extend(
        uid_to_person(person)
        for person in UPLOADERS_SPLIT.split(parsed_dsc.get("Uploaders", ""))
    )

    return IntrinsicPackageMetadata(
        name=p_info.name,
        version=str(p_info.intrinsic_version),
        changelog=changelog,
        maintainers=maintainers,
    )
