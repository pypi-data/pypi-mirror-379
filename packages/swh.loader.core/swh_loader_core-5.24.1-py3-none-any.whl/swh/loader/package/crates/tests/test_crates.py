# Copyright (C) 2022-2025  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information
import json
from pathlib import Path

import pytest
from toml.decoder import TomlDecodeError

from swh.loader.core import __version__
from swh.loader.package.crates.loader import CratesLoader
from swh.loader.tests import assert_last_visit_matches, check_snapshot, get_stats
from swh.model.hashutil import hash_to_bytes
from swh.model.model import (
    MetadataAuthority,
    MetadataAuthorityType,
    MetadataFetcher,
    ObjectType,
    Person,
    RawExtrinsicMetadata,
    Release,
    Snapshot,
    SnapshotBranch,
    SnapshotTargetType,
    TargetType,
    TimestampWithTimezone,
)
from swh.model.swhids import CoreSWHID, ExtendedObjectType, ExtendedSWHID
from swh.model.swhids import ObjectType as OType
from swh.storage.interface import PagedResult


@pytest.fixture
def expected(datadir):
    fp = datadir / Path("expected.json")
    return json.loads(fp.read_bytes())


def test_get_sorted_versions(requests_mock_datadir, swh_storage, expected):
    loader = CratesLoader(
        swh_storage,
        url=expected[1]["url"],
        artifacts=expected[1]["artifacts"],
    )
    assert loader.get_sorted_versions() == [
        "0.1.0",
        "0.1.1",
        "0.1.2",
        "0.2.0",
        "0.2.1",
        "0.3.0",
        "0.3.1",
        "0.4.0",
    ]


def test_get_default_version(requests_mock_datadir, swh_storage, expected):
    loader = CratesLoader(
        swh_storage,
        url=expected[1]["url"],
        artifacts=expected[1]["artifacts"],
    )
    assert loader.get_default_version() == "0.4.0"


def test_crate_invalid_origin_archive_not_found(swh_storage, requests_mock_datadir):
    url = "https://nowhere-to-run/nowhere-to-hide"
    loader = CratesLoader(
        swh_storage,
        url,
        artifacts=[
            {
                "version": "0.0.1",
                "filename": "nowhere-to-hide-0.0.1.crate",
                "url": "https://nowhere-to-run/nowhere-to-hide-0.0.1.crate",
                "checksums": {
                    "sha256": "5de32cb59a062672560d6f0842c4aa7714727457b9fe2daf8987d995a176a405",  # noqa: B950
                },
            },
        ],
    )

    with pytest.raises(Exception):
        assert loader.load() == {"status": "failed"}
        assert_last_visit_matches(
            swh_storage, url, status="not_found", type="crates", snapshot=None
        )


def test_crates_loader_load_one_version(
    datadir, requests_mock_datadir, swh_storage, expected
):
    loader = CratesLoader(
        swh_storage,
        url=expected[0]["url"],
        artifacts=expected[0]["artifacts"],
    )
    actual_load_status = loader.load()
    assert actual_load_status["status"] == "eventful"
    assert actual_load_status["snapshot_id"] is not None

    expected_snapshot_id = "c8f50743fa4fbeef1c94cc5ca3e32155a4dfa12d"
    expected_release_id = "bb6f9b125867a8b4fa0b2febf890a317744e0140"

    assert expected_snapshot_id == actual_load_status["snapshot_id"]

    expected_snapshot = Snapshot(
        id=hash_to_bytes(actual_load_status["snapshot_id"]),
        branches={
            b"releases/0.0.1": SnapshotBranch(
                target=hash_to_bytes(expected_release_id),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"HEAD": SnapshotBranch(
                target=b"releases/0.0.1",
                target_type=SnapshotTargetType.ALIAS,
            ),
        },
    )
    check_snapshot(expected_snapshot, swh_storage)

    stats = get_stats(swh_storage)
    assert {
        "content": 1,
        "directory": 2,
        "origin": 1,
        "origin_visit": 1,
        "release": 1,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1,
    } == stats

    assert swh_storage.release_get([hash_to_bytes(expected_release_id)])[0] == Release(
        name=b"0.0.1",
        message=b"Synthetic release for Crate source package hg-core version 0.0.1\n",
        target=hash_to_bytes("674c3b0b54628d55b93a79dc7adf304efc01b371"),
        target_type=ObjectType.DIRECTORY,
        synthetic=True,
        author=Person.from_fullname(b"Georges Racinet <georges.racinet@octobus.net>"),
        date=TimestampWithTimezone.from_iso8601("2019-04-16T18:48:11.404457+00:00"),
        id=hash_to_bytes(expected_release_id),
    )


def test_crates_loader_load_n_versions(
    datadir, requests_mock_datadir_visits, swh_storage, expected
):
    url = expected[1]["url"]

    loader = CratesLoader(
        swh_storage,
        url=url,
        artifacts=expected[1]["artifacts"],
    )
    actual_load_status = loader.load()

    assert actual_load_status["status"] == "eventful"
    assert actual_load_status["snapshot_id"] is not None

    expected_snapshot_id = "ab068487d16c6ead88960e29990505caad17ed5e"

    assert expected_snapshot_id == actual_load_status["snapshot_id"]

    expected_snapshot = Snapshot(
        id=hash_to_bytes(expected_snapshot_id),
        branches={
            b"releases/0.1.0": SnapshotBranch(
                target=hash_to_bytes("bd8d093b4ad56ca7e49aa0f709d945483b831915"),
                target_type=TargetType.RELEASE,
            ),
            b"releases/0.1.1": SnapshotBranch(
                target=hash_to_bytes("298a08059fef2ecc8298bc9371e9608f4f9d5e6e"),
                target_type=TargetType.RELEASE,
            ),
            b"releases/0.1.2": SnapshotBranch(
                target=hash_to_bytes("e234efbaef1999866d3b5c9a5676c42a5c4d1d3f"),
                target_type=TargetType.RELEASE,
            ),
            b"releases/0.2.0": SnapshotBranch(
                target=hash_to_bytes("519bfdb898f91011eeb618d7d7aaa93097e57ab4"),
                target_type=TargetType.RELEASE,
            ),
            b"releases/0.2.1": SnapshotBranch(
                target=hash_to_bytes("c1bdd5a5a0769c4fd10af92a43e66ce7a2394e8c"),
                target_type=TargetType.RELEASE,
            ),
            b"releases/0.3.0": SnapshotBranch(
                target=hash_to_bytes("d68b74713017c0b32a553f107d179be386bafdbc"),
                target_type=TargetType.RELEASE,
            ),
            b"releases/0.3.1": SnapshotBranch(
                target=hash_to_bytes("ee11442a44d32562aedf731932ae4a8a9cf23feb"),
                target_type=TargetType.RELEASE,
            ),
            b"releases/0.4.0": SnapshotBranch(
                target=hash_to_bytes("0018b25f87d0838f6bef3e94b3000043bc9c938d"),
                target_type=TargetType.RELEASE,
            ),
            b"HEAD": SnapshotBranch(
                target=b"releases/0.4.0",
                target_type=SnapshotTargetType.ALIAS,
            ),
        },
    )

    check_snapshot(expected_snapshot, swh_storage)

    stats = get_stats(swh_storage)
    assert {
        "content": 8,
        "directory": 16,
        "origin": 1,
        "origin_visit": 1,
        "release": 8,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1,
    } == stats

    assert_last_visit_matches(
        swh_storage,
        url,
        status="full",
        type="crates",
        snapshot=expected_snapshot.id,
    )


def test_crates_loader_load_multiple_visits_no_changes(
    datadir, requests_mock_datadir_visits, requests_mock_datadir, swh_storage, expected
):
    url = expected[0]["url"]
    loader = CratesLoader(
        swh_storage,
        url=url,
        artifacts=expected[0]["artifacts"],
    )

    visit_1_actual_load_status = loader.load()
    assert visit_1_actual_load_status["status"] == "eventful"
    assert visit_1_actual_load_status["snapshot_id"] is not None

    expected_snapshot_id = "c8f50743fa4fbeef1c94cc5ca3e32155a4dfa12d"
    expected_release_id = "bb6f9b125867a8b4fa0b2febf890a317744e0140"

    assert expected_snapshot_id == visit_1_actual_load_status["snapshot_id"]

    expected_snapshot = Snapshot(
        id=hash_to_bytes(visit_1_actual_load_status["snapshot_id"]),
        branches={
            b"releases/0.0.1": SnapshotBranch(
                target=hash_to_bytes(expected_release_id),
                target_type=TargetType.RELEASE,
            ),
            b"HEAD": SnapshotBranch(
                target=b"releases/0.0.1",
                target_type=TargetType.ALIAS,
            ),
        },
    )
    check_snapshot(expected_snapshot, swh_storage)

    assert_last_visit_matches(
        swh_storage, url, status="full", type="crates", snapshot=expected_snapshot.id
    )

    stats = get_stats(swh_storage)
    assert {
        "content": 1,
        "directory": 2,
        "origin": 1,
        "origin_visit": 1,
        "release": 1,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1,
    } == stats

    assert swh_storage.release_get([hash_to_bytes(expected_release_id)])[0] == Release(
        name=b"0.0.1",
        message=b"Synthetic release for Crate source package hg-core version 0.0.1\n",
        target=hash_to_bytes("674c3b0b54628d55b93a79dc7adf304efc01b371"),
        target_type=ObjectType.DIRECTORY,
        synthetic=True,
        author=Person.from_fullname(b"Georges Racinet <georges.racinet@octobus.net>"),
        date=TimestampWithTimezone.from_iso8601("2019-04-16T18:48:11.404457+00:00"),
        id=hash_to_bytes(expected_release_id),
    )

    loader_2 = CratesLoader(
        swh_storage,
        url=url,
        artifacts=expected[0]["artifacts"],
    )
    actual_load_status2 = loader_2.load()
    assert actual_load_status2 == {
        "status": "uneventful",
        "snapshot_id": actual_load_status2["snapshot_id"],
    }

    visit_status2 = assert_last_visit_matches(
        swh_storage, url, status="full", type="crates"
    )

    stats2 = get_stats(swh_storage)
    expected_stats2 = stats.copy()
    expected_stats2["origin_visit"] = 1 + 1
    assert expected_stats2 == stats2

    # same snapshot
    assert visit_status2.snapshot == expected_snapshot.id


def test_crates_loader_load_multiple_version_incremental(
    datadir, requests_mock_datadir, swh_storage, expected
):
    url = expected[1]["url"]
    # one version in artifacts
    artifacts_0 = [
        artifact
        for artifact in expected[1]["artifacts"]
        if artifact["version"] in ["0.1.0"]
    ]

    # two versions in artifacts
    artifacts_1 = [
        artifact
        for artifact in expected[1]["artifacts"]
        if artifact["version"] in ["0.1.0", "0.1.1"]
    ]

    # Visit 1
    loader = CratesLoader(
        swh_storage,
        url=url,
        artifacts=artifacts_0,
    )

    visit1_actual_load_status = loader.load()
    visit1_stats = get_stats(swh_storage)
    expected_snapshot_id = hash_to_bytes("e7986b6e255d55bd0ef37bd098d0d4a4c8aefa35")

    assert visit1_actual_load_status == {
        "status": "eventful",
        "snapshot_id": expected_snapshot_id.hex(),
    }

    assert_last_visit_matches(
        swh_storage, url, status="full", type="crates", snapshot=expected_snapshot_id
    )

    assert {
        "content": 1,
        "directory": 2,
        "origin": 1,
        "origin_visit": 1,
        "release": 1,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1,
    } == visit1_stats

    # Visit 2
    loader = CratesLoader(
        swh_storage,
        url=url,
        artifacts=artifacts_1,
    )

    visit2_actual_load_status = loader.load()
    visit2_stats = get_stats(swh_storage)

    assert visit2_actual_load_status["status"] == "eventful", visit2_actual_load_status
    expected_snapshot_id2 = hash_to_bytes("1f7bbf678eeedeef31297bc4273118fde8fe1858")
    assert visit2_actual_load_status == {
        "status": "eventful",
        "snapshot_id": expected_snapshot_id2.hex(),
    }

    assert_last_visit_matches(
        swh_storage, url, status="full", type="crates", snapshot=expected_snapshot_id2
    )
    expected_snapshot = Snapshot(
        id=expected_snapshot_id2,
        branches={
            b"releases/0.1.1": SnapshotBranch(
                target=hash_to_bytes("298a08059fef2ecc8298bc9371e9608f4f9d5e6e"),
                target_type=TargetType.RELEASE,
            ),
            b"releases/0.1.0": SnapshotBranch(
                target=hash_to_bytes("bd8d093b4ad56ca7e49aa0f709d945483b831915"),
                target_type=TargetType.RELEASE,
            ),
            b"HEAD": SnapshotBranch(
                target=b"releases/0.1.1",
                target_type=TargetType.ALIAS,
            ),
        },
    )

    assert_last_visit_matches(
        swh_storage, url, status="full", type="crates", snapshot=expected_snapshot.id
    )

    check_snapshot(expected_snapshot, swh_storage)

    assert {
        "content": 1 + 1,
        "directory": 2 + 2,
        "origin": 1,
        "origin_visit": 1 + 1,
        "release": 1 + 1,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1 + 1,
    } == visit2_stats


def test_crates_loader_raw_extrinsic_metadata(
    datadir, requests_mock_datadir, swh_storage, expected
):
    loader = CratesLoader(
        swh_storage,
        url=expected[0]["url"],
        artifacts=expected[0]["artifacts"],
    )
    actual_load_status = loader.load()
    assert actual_load_status["status"] == "eventful"
    assert actual_load_status["snapshot_id"] is not None

    expected_release_id = "bb6f9b125867a8b4fa0b2febf890a317744e0140"

    release = swh_storage.release_get([hash_to_bytes(expected_release_id)])[0]

    release_swhid = CoreSWHID(
        object_type=OType.RELEASE, object_id=hash_to_bytes(expected_release_id)
    )
    directory_swhid = ExtendedSWHID(
        object_type=ExtendedObjectType.DIRECTORY, object_id=release.target
    )
    metadata_authority = MetadataAuthority(
        type=MetadataAuthorityType.FORGE,
        url="https://crates.io/",
    )
    expected_metadata = [
        RawExtrinsicMetadata(
            target=directory_swhid,
            authority=metadata_authority,
            fetcher=MetadataFetcher(
                name="swh.loader.package.crates.loader.CratesLoader",
                version=__version__,
            ),
            discovery_date=loader.visit_date,
            format="crates-package-json",
            metadata=json.dumps(
                {
                    "audit_actions": [],
                    "bin_names": [],
                    "checksum": "7fe168efadebadb9da6a329fdc027036e233b662285730cad27220e11e53c384",  # noqa
                    "crate": "hg-core",
                    "crate_size": 21344,
                    "created_at": "2019-04-16T18:48:11.404457+00:00",
                    "dl_path": "/api/v1/crates/hg-core/0.0.1/download",
                    "downloads": 1845,
                    "features": {},
                    "has_lib": True,
                    "id": 145309,
                    "lib_links": None,
                    "license": "GPL-2.0-or-later",
                    "links": {
                        "authors": "/api/v1/crates/hg-core/0.0.1/authors",
                        "dependencies": "/api/v1/crates/hg-core/0.0.1/dependencies",
                        "version_downloads": "/api/v1/crates/hg-core/0.0.1/downloads",
                    },
                    "num": "0.0.1",
                    "published_by": {
                        "avatar": "https://avatars0.githubusercontent.com/u/474220?v=4",
                        "id": 45544,
                        "login": "gracinet",
                        "name": "Georges Racinet",
                        "url": "https://github.com/gracinet",
                    },
                    "readme_path": "/api/v1/crates/hg-core/0.0.1/readme",
                    "rust_version": None,
                    "updated_at": "2019-04-16T18:48:11.404457+00:00",
                    "yanked": False,
                }
            ).encode(),
            origin=expected[0]["url"],
            release=release_swhid,
        ),
    ]

    assert swh_storage.raw_extrinsic_metadata_get(
        directory_swhid,
        metadata_authority,
    ) == PagedResult(
        next_page_token=None,
        results=expected_metadata,
    )


def test_crates_loader_toml_decode_error(
    datadir, requests_mock_datadir, swh_storage, expected, mocker
):
    mocker.patch("toml.load").side_effect = TomlDecodeError(msg="foo", doc="bar", pos=0)
    loader = CratesLoader(
        swh_storage,
        url=expected[0]["url"],
        artifacts=expected[0]["artifacts"],
    )
    actual_load_status = loader.load()
    assert actual_load_status["status"] == "eventful"
    assert actual_load_status["snapshot_id"] is not None

    expected_snapshot_id = "1270e5b1cd701a7a74746d98d041f8597a837aae"
    expected_release_id = "e7fed75c18d47011c1809178502d723dd26c73c9"

    assert expected_snapshot_id == actual_load_status["snapshot_id"]

    expected_snapshot = Snapshot(
        id=hash_to_bytes(actual_load_status["snapshot_id"]),
        branches={
            b"releases/0.0.1": SnapshotBranch(
                target=hash_to_bytes(expected_release_id),
                target_type=SnapshotTargetType.RELEASE,
            ),
            b"HEAD": SnapshotBranch(
                target=b"releases/0.0.1",
                target_type=SnapshotTargetType.ALIAS,
            ),
        },
    )
    check_snapshot(expected_snapshot, swh_storage)

    stats = get_stats(swh_storage)
    assert {
        "content": 1,
        "directory": 2,
        "origin": 1,
        "origin_visit": 1,
        "release": 1,
        "revision": 0,
        "skipped_content": 0,
        "snapshot": 1,
    } == stats

    assert swh_storage.release_get([hash_to_bytes(expected_release_id)])[0] == Release(
        name=b"0.0.1",
        message=b"Synthetic release for Crate source package hg-core version 0.0.1\n",
        target=hash_to_bytes("674c3b0b54628d55b93a79dc7adf304efc01b371"),
        target_type=ObjectType.DIRECTORY,
        synthetic=True,
        author=Person.from_fullname(b""),
        date=TimestampWithTimezone.from_iso8601("2019-04-16T18:48:11.404457+00:00"),
        id=hash_to_bytes(expected_release_id),
    )


def test_crates_loader_release_with_multiple_authors(
    datadir, requests_mock_datadir, swh_storage
):
    loader = CratesLoader(
        swh_storage,
        url="https://crates.io/api/v1/crates/clippy",
        artifacts=[
            {
                "version": "0.0.107",
                "checksums": {
                    "sha256": (
                        "99ec3049475544d2330fe515c213fb66"
                        "9b7fa97b1f472443d3798e4ab719071c"
                    ),
                },
                "filename": "clippy-0.0.107.crate",
                "url": ("https://static.crates.io/crates/clippy/clippy-0.0.107.crate"),
            }
        ],
    )
    actual_load_status = loader.load()
    assert actual_load_status["status"] == "eventful"
    assert actual_load_status["snapshot_id"] is not None

    snapshot = loader.last_snapshot()
    release_id = snapshot.branches[b"releases/0.0.107"].target
    release = swh_storage.release_get([release_id])[0]
    assert release.author == Person(
        fullname=b"Manish Goregaokar <manishsmail@gmail.com>",
        name=b"Manish Goregaokar",
        email=b"manishsmail@gmail.com",
    )
    assert release.message == (
        b"Synthetic release for Crate source package clippy version 0.0.107\n\n"
        b"Co-authored-by: Andre Bogus <bogusandre@gmail.com>\n"
        b"Co-authored-by: Georg Brandl <georg@python.org>\n"
        b"Co-authored-by: Martin Carton <cartonmartin@gmail.com>\n"
        b"Co-authored-by: Oliver Schneider <clippy-iethah7aipeen8neex1a@oli-obk.de>\n"
    )
