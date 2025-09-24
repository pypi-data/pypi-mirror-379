# Copyright (C) 2019-2024  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from __future__ import annotations

import json
import logging
import os
from typing import Any, Dict, Iterator, Optional, Sequence, Tuple
from urllib.parse import urlparse

import attr
from pkginfo import UnpackedSDist

from swh.loader.core.utils import (
    EMPTY_AUTHOR,
    cached_method,
    get_url_body,
    release_name,
)
from swh.loader.package.loader import (
    BasePackageInfo,
    PackageLoader,
    PartialExtID,
    RawExtrinsicMetadataCore,
)
from swh.model.hashutil import hash_to_bytes
from swh.model.model import (
    MetadataAuthority,
    MetadataAuthorityType,
    ObjectType,
    Person,
    Release,
    Sha1Git,
    TimestampWithTimezone,
)
from swh.storage.interface import StorageInterface

logger = logging.getLogger(__name__)


EXTID_TYPE = "pypi-archive-sha256"
EXTID_VERSION = 0


@attr.s
class PyPIPackageInfo(BasePackageInfo):
    raw_info = attr.ib(type=Dict[str, Any])

    name = attr.ib(type=str)
    comment_text = attr.ib(type=Optional[str])
    sha256 = attr.ib(type=str)
    upload_time = attr.ib(type=str)

    @classmethod
    def from_metadata(
        cls, metadata: Dict[str, Any], name: str, version: str
    ) -> PyPIPackageInfo:
        return cls(
            url=metadata["url"],
            filename=metadata["filename"],
            version=version,
            raw_info=metadata,
            name=name,
            comment_text=metadata.get("comment_text"),
            sha256=metadata["digests"]["sha256"],
            upload_time=metadata["upload_time"],
            directory_extrinsic_metadata=[
                RawExtrinsicMetadataCore(
                    format="pypi-project-json",
                    metadata=json.dumps(metadata).encode(),
                )
            ],
            checksums={"sha256": metadata["digests"]["sha256"]},
        )

    def extid(self) -> PartialExtID:
        return (EXTID_TYPE, EXTID_VERSION, hash_to_bytes(self.sha256))


class PyPILoader(PackageLoader[PyPIPackageInfo]):
    """Load pypi origin's artifact releases into swh archive."""

    visit_type = "pypi"

    def __init__(self, storage: StorageInterface, url: str, **kwargs):
        super().__init__(storage=storage, url=url, **kwargs)
        self.provider_url = pypi_api_url(self.origin.url)

    @cached_method
    def _raw_info(self) -> bytes:
        return get_url_body(self.provider_url)

    @cached_method
    def info(self) -> Dict:
        """Return the project metadata information (fetched from pypi registry)"""
        return json.loads(self._raw_info())

    def get_versions(self) -> Sequence[str]:
        return list(self.info()["releases"])

    def get_default_version(self) -> str:
        return self.info()["info"]["version"]

    def get_metadata_authority(self):
        p_url = urlparse(self.origin.url)
        return MetadataAuthority(
            type=MetadataAuthorityType.FORGE,
            url=f"{p_url.scheme}://{p_url.netloc}/",
            metadata={},
        )

    def get_package_info(self, version: str) -> Iterator[Tuple[str, PyPIPackageInfo]]:
        res = []
        for meta in self.info()["releases"][version]:
            # process only standard sdist archives
            if meta["packagetype"] != "sdist" or meta["filename"].lower().endswith(
                (".deb", ".egg", ".rpm", ".whl")
            ):
                continue

            p_info = PyPIPackageInfo.from_metadata(
                meta, name=self.info()["info"]["name"], version=version
            )
            res.append((version, p_info))

        if len(res) == 1:
            version, p_info = res[0]
            yield release_name(version), p_info
        else:
            for version, p_info in res:
                yield release_name(version, p_info.filename), p_info

    def build_release(
        self, p_info: PyPIPackageInfo, uncompressed_path: str, directory: Sha1Git
    ) -> Optional[Release]:
        i_metadata = extract_intrinsic_metadata(uncompressed_path)
        if not i_metadata:
            return None

        # from intrinsic metadata
        version_ = i_metadata.get("version", p_info.version)
        author_ = author(i_metadata)

        if p_info.comment_text:
            msg = p_info.comment_text
        else:
            msg = (
                f"Synthetic release for PyPI source package {p_info.name} "
                f"version {version_}\n"
            )

        date = TimestampWithTimezone.from_iso8601(p_info.upload_time)

        return Release(
            name=p_info.version.encode(),
            message=msg.encode(),
            author=author_,
            date=date,
            target=directory,
            target_type=ObjectType.DIRECTORY,
            synthetic=True,
        )


def pypi_api_url(url: str) -> str:
    """Compute api url from a project url

    Args:
        url (str): PyPI instance's url (e.g: https://pypi.org/project/requests)
        This deals with correctly transforming the project's api url (e.g
        https://pypi.org/pypi/requests/json)

    Returns:
        api url

    """
    p_url = urlparse(url)
    project_name = p_url.path.rstrip("/").split("/")[-1]
    url = "%s://%s/pypi/%s/json" % (p_url.scheme, p_url.netloc, project_name)
    return url


def extract_intrinsic_metadata(dir_path: str) -> Dict:
    """Given an uncompressed path holding the pkginfo file, returns a
       pkginfo parsed structure as a dict.

       The release artifact contains at their root one folder. For example:
       $ tar tvf zprint-0.0.6.tar.gz
       drwxr-xr-x root/root         0 2018-08-22 11:01 zprint-0.0.6/
       ...

    Args:

        dir_path (str): Path to the uncompressed directory
                        representing a release artifact from pypi.

    Returns:
        the pkginfo parsed structure as a dict if any or None if
        none was present.

    """
    # Retrieve the root folder of the archive
    if not os.path.exists(dir_path):
        return {}
    lst = os.listdir(dir_path)
    if len(lst) != 1:
        return {}
    project_dirname = lst[0]
    pkginfo_path = os.path.join(dir_path, project_dirname, "PKG-INFO")
    if not os.path.exists(pkginfo_path):
        return {}
    pkginfo = UnpackedSDist(pkginfo_path)
    raw = pkginfo.__dict__
    raw.pop("filename")  # this gets added with the ondisk location
    return raw


def author(data: Dict) -> Person:
    """Given a dict of project/release artifact information (coming from
       PyPI), returns an author subset.

    Args:
        data (dict): Representing either artifact information or
                     release information.

    Returns:
        swh-model dict representing a person.

    """
    name = data.get("author")
    email = data.get("author_email")
    fullname = None  # type: Optional[str]

    if email:
        fullname = "%s <%s>" % (name, email)
    else:
        fullname = name

    if not fullname:
        return EMPTY_AUTHOR

    if name is not None:
        name = name.encode("utf-8")

    if email is not None:
        email = email.encode("utf-8")

    return Person(fullname=fullname.encode("utf-8"), name=name, email=email)
