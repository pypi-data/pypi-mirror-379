# Copyright (C) 2018-2025  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from os import path

import pytest

from swh.core.nar import compute_nar_hashes
from swh.loader.core.utils import compute_hashes


@pytest.fixture
def tarball_path(datadir):
    """Return tarball filepath fetched by TarballDirectoryLoader test runs."""
    return path.join(datadir, "https_example.org", "archives_dummy-hello.tar.gz")


@pytest.fixture
def tarball_with_executable_path(datadir):
    """Return tarball filepath (which contains executable) fetched by
    TarballDirectoryLoader test runs."""
    return path.join(
        datadir, "https_example.org", "archives_dummy-hello-with-executable.tar.gz"
    )


@pytest.fixture
def content_path(datadir):
    """Return filepath fetched by ContentLoader test runs."""
    return path.join(
        datadir, "https_common-lisp.net", "project_asdf_archives_asdf-3.3.5.lisp"
    )


@pytest.fixture
def executable_path(datadir):
    """Return executable filepath fetched by ContentLoader test runs."""
    return path.join(datadir, "https_example.org", "test-executable.sh")


@pytest.fixture
def tarball_with_std_hashes(tarball_path):
    return (
        tarball_path,
        compute_hashes(tarball_path, ["sha1", "sha256", "sha512"]),
    )


@pytest.fixture
def tarball_with_nar_hashes(tarball_path):
    nar_hashes = compute_nar_hashes(tarball_path, ["sha256"])
    # Ensure it's the same hash as the initial one computed from the cli

    assert (
        nar_hashes["sha256"]
        == "45db8a27ccfae60b5233003c54c2d6b5ed6f0a1299dd9bbebc8f06cf649bc9c0"
    )
    return (tarball_path, nar_hashes)


@pytest.fixture
def content_with_nar_hashes(content_path):
    nar_hashes = compute_nar_hashes(content_path, ["sha256"], is_tarball=False)
    # Ensure it's the same hash as the initial one computed from the cli
    assert (
        nar_hashes["sha256"]
        == "0b555a4d13e530460425d1dc20332294f151067fb64a7e49c7de501f05b0a41a"
    )
    return (content_path, nar_hashes)
