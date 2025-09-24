# Copyright (C) 2019-2021 The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

import json
import os
from os import path
from unittest.mock import patch

import pytest

from swh.core.pytest_plugin import requests_mock_datadir_factory
from swh.core.tarball import uncompress
from swh.loader.core import __version__
from swh.loader.package.pypi.loader import (
    PyPILoader,
    PyPIPackageInfo,
    author,
    extract_intrinsic_metadata,
    pypi_api_url,
)
from swh.loader.tests import assert_last_visit_matches, check_snapshot, get_stats
from swh.model.hashutil import hash_to_bytes
from swh.model.model import (
    MetadataAuthority,
    MetadataAuthorityType,
    MetadataFetcher,
    Person,
    RawExtrinsicMetadata,
    Snapshot,
    SnapshotBranch,
    SnapshotTargetType,
)
from swh.model.swhids import CoreSWHID, ExtendedObjectType, ExtendedSWHID, ObjectType
from swh.storage.interface import PagedResult


@pytest.fixture
def _0805nexter_api_info(datadir) -> bytes:
    with open(
        os.path.join(datadir, "https_pypi.org", "pypi_0805nexter_json"),
        "rb",
    ) as f:
        return f.read()


def test_pypi_author_basic():
    data = {
        "author": "i-am-groot",
        "author_email": "iam@groot.org",
    }
    actual_author = author(data)

    expected_author = Person(
        fullname=b"i-am-groot <iam@groot.org>",
        name=b"i-am-groot",
        email=b"iam@groot.org",
    )

    assert actual_author == expected_author


def test_pypi_author_empty_email():
    data = {
        "author": "i-am-groot",
        "author_email": "",
    }
    actual_author = author(data)

    expected_author = Person(
        fullname=b"i-am-groot",
        name=b"i-am-groot",
        email=b"",
    )

    assert actual_author == expected_author


def test_pypi_author_empty_name():
    data = {
        "author": "",
        "author_email": "iam@groot.org",
    }
    actual_author = author(data)

    expected_author = Person(
        fullname=b" <iam@groot.org>",
        name=b"",
        email=b"iam@groot.org",
    )

    assert actual_author == expected_author


def test_pypi_author_malformed():
    data = {
        "author": "['pierre', 'paul', 'jacques']",
        "author_email": None,
    }

    actual_author = author(data)

    expected_author = Person(
        fullname=b"['pierre', 'paul', 'jacques']",
        name=b"['pierre', 'paul', 'jacques']",
        email=None,
    )

    assert actual_author == expected_author


def test_pypi_author_malformed_2():
    data = {
        "author": "[marie, jeanne]",
        "author_email": "[marie@some, jeanne@thing]",
    }

    actual_author = author(data)

    expected_author = Person(
        fullname=b"[marie, jeanne] <[marie@some, jeanne@thing]>",
        name=b"[marie, jeanne]",
        email=b"[marie@some, jeanne@thing]",
    )

    assert actual_author == expected_author


def test_pypi_author_malformed_3():
    data = {
        "author": "[marie, jeanne, pierre]",
        "author_email": "[marie@somewhere.org, jeanne@somewhere.org]",
    }

    actual_author = author(data)

    expected_author = Person(
        fullname=(
            b"[marie, jeanne, pierre] " b"<[marie@somewhere.org, jeanne@somewhere.org]>"
        ),
        name=b"[marie, jeanne, pierre]",
        email=b"[marie@somewhere.org, jeanne@somewhere.org]",
    )

    actual_author == expected_author


# configuration error #


def test_pypi_api_url():
    """Compute pypi api url from the pypi project url should be ok"""
    url = pypi_api_url("https://pypi.org/project/requests")
    assert url == "https://pypi.org/pypi/requests/json"


def test_pypi_api_url_with_slash():
    """Compute pypi api url from the pypi project url should be ok"""
    url = pypi_api_url("https://pypi.org/project/requests/")
    assert url == "https://pypi.org/pypi/requests/json"


def test_pypi_extract_intrinsic_metadata(tmp_path, datadir):
    """Parsing existing archive's PKG-INFO should yield results"""
    uncompressed_archive_path = str(tmp_path)
    archive_path = path.join(
        datadir, "https_files.pythonhosted.org", "0805nexter-1.1.0.zip"
    )
    uncompress(archive_path, dest=uncompressed_archive_path)

    actual_metadata = extract_intrinsic_metadata(uncompressed_archive_path)
    expected_metadata = {
        "metadata_version": "1.0",
        "name": "0805nexter",
        "version": "1.1.0",
        "summary": "a simple printer of nested lest",
        "home_page": "http://www.hp.com",
        "author": "hgtkpython",
        "author_email": "2868989685@qq.com",
        "platforms": ["UNKNOWN"],
    }

    assert actual_metadata == expected_metadata


def test_pypi_extract_intrinsic_metadata_failures(tmp_path):
    """Parsing inexistent path/archive/PKG-INFO yield None"""
    tmp_path = str(tmp_path)  # py3.5 work around (PosixPath issue)
    # inexistent first level path
    assert extract_intrinsic_metadata("/something-inexistent") == {}
    # inexistent second level path (as expected by pypi archives)
    assert extract_intrinsic_metadata(tmp_path) == {}
    # inexistent PKG-INFO within second level path
    existing_path_no_pkginfo = path.join(tmp_path, "something")
    os.mkdir(existing_path_no_pkginfo)
    assert extract_intrinsic_metadata(tmp_path) == {}


# LOADER SCENARIO #

# "edge" cases (for the same origin) #


# no release artifact:
# {visit full, status: uneventful, no contents, etc...}
requests_mock_datadir_missing_all = requests_mock_datadir_factory(
    ignore_urls=[
        "https://files.pythonhosted.org/packages/ec/65/c0116953c9a3f47de89e71964d6c7b0c783b01f29fa3390584dbf3046b4d/0805nexter-1.1.0.zip",  # noqa
        "https://files.pythonhosted.org/packages/c4/a0/4562cda161dc4ecbbe9e2a11eb365400c0461845c5be70d73869786809c4/0805nexter-1.2.0.zip",  # noqa
    ]
)


def test_pypi_no_release_artifact(swh_storage, requests_mock_datadir_missing_all):
    """Load a pypi project with all artifacts missing ends up with no snapshot"""
    url = "https://pypi.org/project/0805nexter"
    loader = PyPILoader(swh_storage, url)

    actual_load_status = loader.load()
    assert actual_load_status["status"] == "uneventful"
    assert actual_load_status["snapshot_id"] is not None

    empty_snapshot = Snapshot(branches={})

    assert_last_visit_matches(
        swh_storage, url, status="partial", type="pypi", snapshot=empty_snapshot.id
    )

    stats = get_stats(swh_storage)
    assert {
        "content": 0,
        "directory": 0,
        "origin": 1,
        "origin_visit": 1,
        "release": 0,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1,
    } == stats


def test_pypi_fail__load_snapshot(swh_storage, requests_mock_datadir):
    """problem during loading: {visit: failed, status: failed, no snapshot}"""
    url = "https://pypi.org/project/0805nexter"
    with patch(
        "swh.loader.package.pypi.loader.PyPILoader._load_snapshot",
        side_effect=ValueError("Fake problem to fail visit"),
    ):
        loader = PyPILoader(swh_storage, url)

        actual_load_status = loader.load()
        assert actual_load_status == {"status": "failed"}

        assert_last_visit_matches(swh_storage, url, status="failed", type="pypi")

        stats = get_stats(loader.storage)

        assert {
            "content": 6,
            "directory": 4,
            "origin": 1,
            "origin_visit": 1,
            "release": 2,
            "revision": 0,
            "skipped_content": 0,
            "snapshot": 0,
        } == stats


# problem during loading:
# {visit: partial, status: uneventful, no snapshot}


def test_pypi_release_with_traceback(swh_storage, requests_mock_datadir):
    url = "https://pypi.org/project/0805nexter"
    with patch(
        "swh.loader.package.pypi.loader.PyPILoader.last_snapshot",
        side_effect=ValueError("Fake problem to fail the visit"),
    ):
        loader = PyPILoader(swh_storage, url)

        actual_load_status = loader.load()
        assert actual_load_status == {"status": "failed"}

        assert_last_visit_matches(swh_storage, url, status="failed", type="pypi")

        stats = get_stats(swh_storage)

        assert {
            "content": 0,
            "directory": 0,
            "origin": 1,
            "origin_visit": 1,
            "release": 0,
            "revision": 0,
            "skipped_content": 0,
            "snapshot": 0,
        } == stats


# problem during loading: failure early enough in between swh contents...
# some contents (contents, directories, etc...) have been written in storage
# {visit: partial, status: eventful, no snapshot}

# problem during loading: failure late enough we can have snapshots (some
# revisions are written in storage already)
# {visit: partial, status: eventful, snapshot}

# "normal" cases (for the same origin) #


requests_mock_datadir_missing_one = requests_mock_datadir_factory(
    ignore_urls=[
        "https://files.pythonhosted.org/packages/ec/65/c0116953c9a3f47de89e71964d6c7b0c783b01f29fa3390584dbf3046b4d/0805nexter-1.1.0.zip",  # noqa
    ]
)

# some missing release artifacts:
# {visit partial, status: eventful, 1 snapshot}


def test_pypi_release_metadata_structure(
    swh_storage, requests_mock_datadir, _0805nexter_api_info
):
    url = "https://pypi.org/project/0805nexter"
    loader = PyPILoader(swh_storage, url)

    actual_load_status = loader.load()
    assert actual_load_status["status"] == "eventful"
    assert actual_load_status["snapshot_id"] is not None

    expected_release_id = hash_to_bytes("fbbcb817f01111b06442cdcc93140ab3cc777d68")

    expected_snapshot = Snapshot(
        id=hash_to_bytes(actual_load_status["snapshot_id"]),
        branches={
            b"HEAD": SnapshotBranch(
                target=b"releases/1.2.0",
                target_type=SnapshotTargetType.ALIAS,
            ),
            b"releases/1.1.0": SnapshotBranch(
                target=hash_to_bytes("f8789ff3ed70a5f570c35d885c7bcfda7b23b091"),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"releases/1.2.0": SnapshotBranch(
                target=expected_release_id,
                target_type=SnapshotTargetType.RELEASE,
            ),
        },
    )

    assert_last_visit_matches(
        swh_storage, url, status="full", type="pypi", snapshot=expected_snapshot.id
    )

    check_snapshot(expected_snapshot, swh_storage)

    release = swh_storage.release_get([expected_release_id])[0]
    assert release is not None

    release_swhid = CoreSWHID(
        object_type=ObjectType.RELEASE, object_id=expected_release_id
    )
    directory_swhid = ExtendedSWHID(
        object_type=ExtendedObjectType.DIRECTORY, object_id=release.target
    )
    metadata_authority = MetadataAuthority(
        type=MetadataAuthorityType.FORGE,
        url="https://pypi.org/",
    )
    expected_metadata = [
        RawExtrinsicMetadata(
            target=directory_swhid,
            authority=metadata_authority,
            fetcher=MetadataFetcher(
                name="swh.loader.package.pypi.loader.PyPILoader",
                version=__version__,
            ),
            discovery_date=loader.visit_date,
            format="pypi-project-json",
            metadata=json.dumps(
                json.loads(_0805nexter_api_info)["releases"]["1.2.0"][0]
            ).encode(),
            origin=url,
            release=release_swhid,
        )
    ]
    assert swh_storage.raw_extrinsic_metadata_get(
        directory_swhid,
        metadata_authority,
    ) == PagedResult(
        next_page_token=None,
        results=expected_metadata,
    )


def test_pypi_visit_with_missing_artifact(
    swh_storage, requests_mock_datadir_missing_one
):
    """Load a pypi project with some missing artifacts ends up with 1 snapshot"""
    url = "https://pypi.org/project/0805nexter"
    loader = PyPILoader(swh_storage, url)

    actual_load_status = loader.load()
    expected_snapshot_id = hash_to_bytes("00785a38479abe5fbfa402df96be26d2ddf89c97")
    assert actual_load_status == {
        "status": "eventful",
        "snapshot_id": expected_snapshot_id.hex(),
    }

    assert_last_visit_matches(
        swh_storage,
        url,
        status="partial",
        type="pypi",
        snapshot=expected_snapshot_id,
    )

    expected_snapshot = Snapshot(
        id=hash_to_bytes(expected_snapshot_id),
        branches={
            b"releases/1.2.0": SnapshotBranch(
                target=hash_to_bytes("fbbcb817f01111b06442cdcc93140ab3cc777d68"),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"HEAD": SnapshotBranch(
                target=b"releases/1.2.0",
                target_type=SnapshotTargetType.ALIAS,
            ),
        },
    )
    check_snapshot(expected_snapshot, storage=swh_storage)

    stats = get_stats(swh_storage)

    assert {
        "content": 3,
        "directory": 2,
        "origin": 1,
        "origin_visit": 1,
        "release": 1,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1,
    } == stats


def test_pypi_visit_with_1_release_artifact(swh_storage, requests_mock_datadir):
    """With no prior visit, load a pypi project ends up with 1 snapshot"""
    url = "https://pypi.org/project/0805nexter"
    loader = PyPILoader(swh_storage, url)

    actual_load_status = loader.load()
    expected_snapshot_id = hash_to_bytes("3dd50c1a0e48a7625cf1427e3190a65b787c774e")
    assert actual_load_status == {
        "status": "eventful",
        "snapshot_id": expected_snapshot_id.hex(),
    }

    assert_last_visit_matches(
        swh_storage, url, status="full", type="pypi", snapshot=expected_snapshot_id
    )

    expected_snapshot = Snapshot(
        id=expected_snapshot_id,
        branches={
            b"releases/1.1.0": SnapshotBranch(
                target=hash_to_bytes("f8789ff3ed70a5f570c35d885c7bcfda7b23b091"),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"releases/1.2.0": SnapshotBranch(
                target=hash_to_bytes("fbbcb817f01111b06442cdcc93140ab3cc777d68"),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"HEAD": SnapshotBranch(
                target=b"releases/1.2.0",
                target_type=SnapshotTargetType.ALIAS,
            ),
        },
    )
    check_snapshot(expected_snapshot, swh_storage)

    stats = get_stats(swh_storage)
    assert {
        "content": 6,
        "directory": 4,
        "origin": 1,
        "origin_visit": 1,
        "release": 2,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1,
    } == stats


def test_pypi_multiple_visits_with_no_change(swh_storage, requests_mock_datadir):
    """Multiple visits with no changes results in 1 same snapshot"""
    url = "https://pypi.org/project/0805nexter"
    loader = PyPILoader(swh_storage, url)

    actual_load_status = loader.load()
    snapshot_id = hash_to_bytes("3dd50c1a0e48a7625cf1427e3190a65b787c774e")
    assert actual_load_status == {
        "status": "eventful",
        "snapshot_id": snapshot_id.hex(),
    }
    assert_last_visit_matches(
        swh_storage, url, status="full", type="pypi", snapshot=snapshot_id
    )

    expected_snapshot = Snapshot(
        id=snapshot_id,
        branches={
            b"releases/1.1.0": SnapshotBranch(
                target=hash_to_bytes("f8789ff3ed70a5f570c35d885c7bcfda7b23b091"),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"releases/1.2.0": SnapshotBranch(
                target=hash_to_bytes("fbbcb817f01111b06442cdcc93140ab3cc777d68"),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"HEAD": SnapshotBranch(
                target=b"releases/1.2.0",
                target_type=SnapshotTargetType.ALIAS,
            ),
        },
    )
    check_snapshot(expected_snapshot, swh_storage)

    stats = get_stats(swh_storage)

    assert {
        "content": 6,
        "directory": 4,
        "origin": 1,
        "origin_visit": 1,
        "release": 2,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1,
    } == stats

    actual_load_status2 = loader.load()
    assert actual_load_status2 == {
        "status": "uneventful",
        "snapshot_id": actual_load_status2["snapshot_id"],
    }

    visit_status2 = assert_last_visit_matches(
        swh_storage, url, status="full", type="pypi"
    )

    stats2 = get_stats(swh_storage)
    expected_stats2 = stats.copy()
    expected_stats2["origin_visit"] = 1 + 1
    assert expected_stats2 == stats2

    # same snapshot
    assert visit_status2.snapshot == snapshot_id


def test_pypi_incremental_visit(swh_storage, requests_mock_datadir_visits):
    """With prior visit, 2nd load will result with a different snapshot"""
    url = "https://pypi.org/project/0805nexter"
    loader = PyPILoader(swh_storage, url)

    visit1_actual_load_status = loader.load()
    visit1_stats = get_stats(swh_storage)
    expected_snapshot_id = hash_to_bytes("3dd50c1a0e48a7625cf1427e3190a65b787c774e")
    assert visit1_actual_load_status == {
        "status": "eventful",
        "snapshot_id": expected_snapshot_id.hex(),
    }

    assert_last_visit_matches(
        swh_storage, url, status="full", type="pypi", snapshot=expected_snapshot_id
    )

    assert {
        "content": 6,
        "directory": 4,
        "origin": 1,
        "origin_visit": 1,
        "release": 2,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1,
    } == visit1_stats

    # Reset internal state
    del loader._cached__raw_info
    del loader._cached_info

    visit2_actual_load_status = loader.load()
    visit2_stats = get_stats(swh_storage)

    assert visit2_actual_load_status["status"] == "eventful", visit2_actual_load_status
    expected_snapshot_id2 = hash_to_bytes("77febe6ff0faf6cc00dd015a6c9763579a9fb6c7")
    assert visit2_actual_load_status == {
        "status": "eventful",
        "snapshot_id": expected_snapshot_id2.hex(),
    }

    assert_last_visit_matches(
        swh_storage, url, status="full", type="pypi", snapshot=expected_snapshot_id2
    )

    expected_snapshot = Snapshot(
        id=expected_snapshot_id2,
        branches={
            b"releases/1.1.0": SnapshotBranch(
                target=hash_to_bytes("f8789ff3ed70a5f570c35d885c7bcfda7b23b091"),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"releases/1.2.0": SnapshotBranch(
                target=hash_to_bytes("fbbcb817f01111b06442cdcc93140ab3cc777d68"),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"releases/1.3.0": SnapshotBranch(
                target=hash_to_bytes("a21b09cbec8e31f47307f196bb1f939effc26e11"),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"HEAD": SnapshotBranch(
                target=b"releases/1.3.0",
                target_type=SnapshotTargetType.ALIAS,
            ),
        },
    )

    assert_last_visit_matches(
        swh_storage, url, status="full", type="pypi", snapshot=expected_snapshot.id
    )

    check_snapshot(expected_snapshot, swh_storage)

    assert {
        "content": 6 + 1,  # 1 more content
        "directory": 4 + 2,  # 2 more directories
        "origin": 1,
        "origin_visit": 1 + 1,
        "release": 2 + 1,  # 1 more release
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1 + 1,  # 1 more snapshot
    } == visit2_stats

    urls = [
        m.url
        for m in requests_mock_datadir_visits.request_history
        if m.url.startswith("https://files.pythonhosted.org")
    ]
    # visited each artifact once across 2 visits
    assert len(urls) == len(set(urls))


# release artifact, no new artifact
# {visit full, status uneventful, same snapshot as before}

# release artifact, old artifact with different checksums
# {visit full, status full, new snapshot with shared history and some new
# different history}

# release with multiple sdist artifacts per pypi "version"
# snapshot branch output is different


def test_pypi_visit_1_release_with_2_artifacts(swh_storage, requests_mock_datadir):
    """With no prior visit, load a pypi project ends up with 1 snapshot"""
    url = "https://pypi.org/project/nexter"
    loader = PyPILoader(swh_storage, url)

    actual_load_status = loader.load()
    expected_snapshot_id = hash_to_bytes("1394b2e59351a944cc763bd9d26d90ce8e8121a8")
    assert actual_load_status == {
        "status": "eventful",
        "snapshot_id": expected_snapshot_id.hex(),
    }

    assert_last_visit_matches(
        swh_storage, url, status="full", type="pypi", snapshot=expected_snapshot_id
    )

    expected_snapshot = Snapshot(
        id=expected_snapshot_id,
        branches={
            b"releases/1.1.0/nexter-1.1.0.zip": SnapshotBranch(
                target=hash_to_bytes("f7d43faeb65b64d3faa67e4f46559db57d26b9a4"),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"releases/1.1.0/nexter-1.1.0.tar.gz": SnapshotBranch(
                target=hash_to_bytes("732bb9dc087e6015884daaebb8b82559be729b5a"),
                target_type=SnapshotTargetType.RELEASE,
            ),
        },
    )
    check_snapshot(expected_snapshot, swh_storage)


def test_pypi_artifact_with_no_intrinsic_metadata(swh_storage, requests_mock_datadir):
    """Skip artifact with no intrinsic metadata during ingestion"""
    url = "https://pypi.org/project/upymenu"
    loader = PyPILoader(swh_storage, url)

    actual_load_status = loader.load()
    expected_snapshot_id = hash_to_bytes("1a8893e6a86f444e8be8e7bda6cb34fb1735a00e")
    assert actual_load_status == {
        "status": "eventful",
        "snapshot_id": expected_snapshot_id.hex(),
    }

    # no branch as one artifact without any intrinsic metadata
    expected_snapshot = Snapshot(id=expected_snapshot_id, branches={})

    assert_last_visit_matches(
        swh_storage, url, status="full", type="pypi", snapshot=expected_snapshot.id
    )

    check_snapshot(expected_snapshot, swh_storage)


def test_pypi_origin_not_found(swh_storage, requests_mock_datadir):
    url = "https://pypi.org/project/unknown"
    loader = PyPILoader(swh_storage, url)

    assert loader.load() == {"status": "failed"}

    assert_last_visit_matches(
        swh_storage, url, status="not_found", type="pypi", snapshot=None
    )


def test_pypi_build_release_missing_version_in_pkg_info(swh_storage, tmp_path):
    """Simulate release build when Version field is missing in PKG-INFO file."""
    url = "https://pypi.org/project/GermlineFilter"
    # create package info
    p_info = PyPIPackageInfo(
        url=url,
        filename="GermlineFilter-1.2.tar.gz",
        version="1.2",
        name="GermlineFilter",
        directory_extrinsic_metadata=[],
        raw_info={},
        comment_text="",
        sha256="e4982353c544d94b34f02c5690ab3d3ebc93480d5b62fe6f3317f23c515acc05",
        upload_time="2015-02-18T20:39:13",
    )

    # create PKG-INFO file with missing Version field
    package_path = tmp_path / "GermlineFilter-1.2"
    pkg_info_path = package_path / "PKG-INFO"
    package_path.mkdir()
    pkg_info_path.write_text(
        """Metadata-Version: 1.2
Name: germline_filter
Home-page:
Author: Cristian Caloian (OICR)
Author-email: cristian.caloian@oicr.on.ca
License: UNKNOWN
Description: UNKNOWN
Platform: UNKNOWN"""
    )
    directory = hash_to_bytes("8b864d66f356afe35033d58f8e03b7c23a66751f")

    # attempt to build release
    loader = PyPILoader(swh_storage, url)
    release = loader.build_release(p_info, str(tmp_path), directory)

    # without comment_text and version in PKG-INFO, message should be empty
    assert (
        release.message
        == b"Synthetic release for PyPI source package GermlineFilter version 1.2\n"
    )


def test_filter_out_invalid_sdists(swh_storage, requests_mock):
    project_name = "swh-test-sdist-filtering"
    version = "1.0.0"
    url = f"https://pypi.org/project/{project_name}"
    json_url = f"https://pypi.org/pypi/{project_name}/json"

    common_sdist_entries = {
        "url": "",
        "comment_text": "",
        "digests": {"sha256": ""},
        "upload_time": "",
        "packagetype": "sdist",
    }

    requests_mock.get(
        json_url,
        json={
            "info": {
                "name": project_name,
            },
            "releases": {
                version: [
                    {
                        **common_sdist_entries,
                        "filename": f"{project_name}-{version}.{ext}",
                    }
                    for ext in ("tar.gz", "deb", "egg", "rpm", "whl")
                ]
            },
        },
    )

    loader = PyPILoader(swh_storage, url)

    packages = list(loader.get_package_info(version=version))

    assert len(packages) == 1
    assert packages[0][1].filename.endswith(".tar.gz")
