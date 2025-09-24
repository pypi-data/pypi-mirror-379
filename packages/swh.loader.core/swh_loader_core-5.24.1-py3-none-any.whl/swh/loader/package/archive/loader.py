# Copyright (C) 2019-2024  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from __future__ import annotations

import datetime
import hashlib
import logging
from os import path
import string
from typing import Any, Dict, Iterator, Mapping, Optional, Sequence, Tuple, Union

import attr
import iso8601

from swh.loader.core.utils import EMPTY_AUTHOR, release_name
from swh.loader.package.loader import BasePackageInfo, PackageLoader, PartialExtID
from swh.model.model import ObjectType, Release, Sha1Git, TimestampWithTimezone
from swh.storage.interface import StorageInterface

logger = logging.getLogger(__name__)


@attr.s
class ArchivePackageInfo(BasePackageInfo):
    raw_info = attr.ib(type=Dict[str, Any])
    length = attr.ib(type=int)
    """Size of the archive file"""
    time = attr.ib(type=Union[str, datetime.datetime])
    """Timestamp of the archive file on the server"""

    # default format for gnu
    MANIFEST_FORMAT = string.Template("$time $length $version $url")

    def extid(self, manifest_format: Optional[string.Template] = None) -> PartialExtID:
        """Returns a unique intrinsic identifier of this package info

        ``manifest_format`` allows overriding the class' default MANIFEST_FORMAT"""
        manifest_format = manifest_format or self.MANIFEST_FORMAT
        # TODO: use parsed attributes instead of self.raw_info
        manifest = manifest_format.substitute(
            {k: str(v) for (k, v) in self.raw_info.items()}
        )
        return (
            self.EXTID_TYPE,
            self.EXTID_VERSION,
            hashlib.sha256(manifest.encode()).digest(),
        )

    @classmethod
    def from_metadata(cls, a_metadata: Dict[str, Any]) -> ArchivePackageInfo:
        url = a_metadata["url"]
        filename = a_metadata.get("filename")
        return cls(
            url=url,
            filename=filename if filename else path.split(url)[-1],
            raw_info=a_metadata,
            length=a_metadata["length"],
            time=a_metadata["time"],
            version=a_metadata["version"],
            checksums={"length": a_metadata["length"]},
        )


class ArchiveLoader(PackageLoader[ArchivePackageInfo]):
    """Load archive origin's artifact files into swh archive"""

    visit_type = "tar"

    def __init__(
        self,
        storage: StorageInterface,
        url: str,
        artifacts: Sequence[Dict[str, Any]],
        extid_manifest_format: Optional[str] = None,
        snapshot_append: bool = False,
        **kwargs: Any,
    ):
        f"""Loader constructor.

        For now, this is the lister's task output.

        Args:
            url: Origin url
            artifacts: List of artifact information with keys:

               - **time**: last modification time as either isoformat date
                 string or timestamp

               - **url**: the artifact url to retrieve filename

               - **filename**: optionally, the file's name

               - **version**: artifact's version

               - **length**: artifact's length

            extid_manifest_format: template string used to format a manifest,
                which is hashed to get the extid of a package.
                Defaults to {ArchivePackageInfo.MANIFEST_FORMAT!r}
            snapshot_append: if :const:`True`, append latest snapshot content to
                the new snapshot created by the loader

        """
        super().__init__(storage=storage, url=url, **kwargs)
        self.artifacts = artifacts  # assume order is enforced in the lister
        self.extid_manifest_format = (
            None
            if extid_manifest_format is None
            else string.Template(extid_manifest_format)
        )
        self.snapshot_append = snapshot_append

    def get_versions(self) -> Sequence[str]:
        versions = []
        for archive in self.artifacts:
            v = archive.get("version")
            if v:
                versions.append(v)
        return versions

    def get_package_info(
        self, version: str
    ) -> Iterator[Tuple[str, ArchivePackageInfo]]:
        for a_metadata in self.artifacts:
            p_info = ArchivePackageInfo.from_metadata(a_metadata)
            if version == p_info.version:
                # FIXME: this code assumes we have only 1 artifact per
                # versioned package
                yield release_name(version), p_info

    def new_packageinfo_to_extid(
        self, p_info: ArchivePackageInfo
    ) -> Optional[PartialExtID]:
        return p_info.extid(manifest_format=self.extid_manifest_format)

    def build_release(
        self, p_info: ArchivePackageInfo, uncompressed_path: str, directory: Sha1Git
    ) -> Optional[Release]:
        time = p_info.time  # assume it's a timestamp
        if isinstance(time, str):  # otherwise, assume it's a parsable date
            parsed_time = iso8601.parse_date(time)
        else:
            parsed_time = time
        normalized_time = (
            TimestampWithTimezone.from_datetime(parsed_time)
            if parsed_time is not None
            else None
        )
        msg = f"Synthetic release for archive at {p_info.url}\n"
        return Release(
            name=p_info.version.encode(),
            message=msg.encode(),
            date=normalized_time,
            author=EMPTY_AUTHOR,
            target=directory,
            target_type=ObjectType.DIRECTORY,
            synthetic=True,
        )

    def extra_branches(self) -> Dict[bytes, Mapping[str, Any]]:
        if not self.snapshot_append:
            return {}
        last_snapshot = self.last_snapshot()
        return last_snapshot.to_dict()["branches"] if last_snapshot else {}
