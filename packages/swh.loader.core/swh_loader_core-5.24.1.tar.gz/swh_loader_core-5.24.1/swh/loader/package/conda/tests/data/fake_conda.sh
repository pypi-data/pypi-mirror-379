#!/usr/bin/env bash

# Script to generate fake Conda package archives as .tar.gz.

set -euo pipefail

# Create directories
readonly TMP=tmp_dir/cpan
readonly BASE_PATH=https_conda.anaconda.org

mkdir -p $TMP

# tar.gz package archives
# Conda package tar.gz archive needs at least one 'info' directory to store json
# or yaml metadata

mkdir -p $BASE_PATH

mkdir -p ${TMP}/lifetimes-0.11.1-py36h9f0ad1d_1/info/

mkdir -p ${TMP}/lifetimes-0.11.1-py36hc560c46_1/info/recipe/

echo -e '''{
  "channels": [
    "conda-forge",
    "defaults",
    "https://conda.anaconda.org/conda-forge"
  ],
  "conda_build_version": "3.19.2",
  "conda_private": false,
  "conda_version": "4.8.3",
  "doc_url": "https://lifetimes.readthedocs.io/en/latest/?badge=latest",
  "env_vars": {
    "CIO_TEST": "<not set>"
  },
  "extra": {
    "copy_test_source_files": true,
    "final": true,
    "recipe-maintainers": [
      "CamDavidsonPilon",
      "Arnoldosmium"
    ]
  },
  "home": "https://github.com/CamDavidsonPilon/lifetimes",
  "identifiers": [],
  "keywords": [],
  "license": "MIT",
  "license_family": "MIT",
  "license_file": "README.md",
  "root_pkgs": [
    "yaml 0.2.5 h516909a_0",
    "python-libarchive-c 2.9 py37_0",
    "openssl 1.1.1g h516909a_0",
    "lzo 2.10 h14c3975_1000",
    "pkginfo 1.5.0.1 py_0",
    "git 2.27.0 pl526h5e3e691_0",
    "libgcc-ng 9.2.0 h24d8f2e_2",
    "perl 5.26.2 h516909a_1006",
    "gettext 0.19.8.1 hc5be6a0_1002",
    "libarchive 3.3.3 h3a8160c_1008",
    "libiconv 1.15 h516909a_1006",
    "wheel 0.34.2 py_1",
    "libstdcxx-ng 9.2.0 hdf63c60_2",
    "attrs 19.3.0 py_0",
    "libgomp 9.2.0 h24d8f2e_2",
    "bzip2 1.0.8 h516909a_2",
    "jsonschema 3.2.0 py37hc8dfbb8_1",
    "tk 8.6.10 hed695b0_0",
    "icu 67.1 he1b5a44_0",
    "cffi 1.14.0 py37hd463f26_0",
    "psutil 5.7.0 py37h8f50634_1",
    "_libgcc_mutex 0.1 conda_forge",
    "pycosat 0.6.3 py37h8f50634_1004",
    "python_abi 3.7 1_cp37m",
    "tini 0.18.0 h14c3975_1001",
    "ruamel_yaml 0.15.80 py37h8f50634_1001",
    "readline 8.0 hf8c457e_0",
    "jinja2 2.11.2 pyh9f0ad1d_0",
    "idna 2.10 pyh9f0ad1d_0",
    "soupsieve 2.0.1 py37hc8dfbb8_0",
    "nbformat 5.0.6 py_0",
    "expat 2.2.9 he1b5a44_2",
    "six 1.15.0 pyh9f0ad1d_0",
    "clyent 1.2.2 py_1",
    "pcre 8.44 he1b5a44_0",
    "setuptools 49.1.0 py37hc8dfbb8_0",
    "libssh2 1.9.0 hab1572f_2",
    "pysocks 1.7.1 py37hc8dfbb8_1",
    "sqlite 3.32.3 hcee41ef_0",
    "pyopenssl 19.1.0 py_1",
    "certifi 2020.6.20 py37hc8dfbb8_0",
    "zipp 3.1.0 py_0",
    "ipython_genutils 0.2.0 py_1",
    "pyrsistent 0.16.0 py37h8f50634_0",
    "importlib-metadata 1.7.0 py37hc8dfbb8_0",
    "brotlipy 0.7.0 py37h8f50634_1000",
    "markupsafe 1.1.1 py37h8f50634_1",
    "chardet 3.0.4 py37hc8dfbb8_1006",
    "importlib_metadata 1.7.0 0",
    "ld_impl_linux-64 2.34 h53a641e_5",
    "ncurses 6.1 hf484d3e_1002",
    "_openmp_mutex 4.5 0_gnu",
    "libcurl 7.71.1 hcdd3856_0",
    "ca-certificates 2020.6.20 hecda079_0",
    "pyyaml 5.3.1 py37h8f50634_0",
    "lz4-c 1.9.2 he1b5a44_1",
    "libedit 3.1.20191231 h46ee950_0",
    "su-exec 0.2 h516909a_1002",
    "libffi 3.2.1 he1b5a44_1007",
    "patchelf 0.11 he1b5a44_0",
    "python 3.7.6 cpython_h8356626_6",
    "conda 4.8.3 py37hc8dfbb8_1",
    "tqdm 4.47.0 pyh9f0ad1d_0",
    "cryptography 2.9.2 py37hb09aad4_0",
    "pycparser 2.20 pyh9f0ad1d_2",
    "glob2 0.7 py_0",
    "zlib 1.2.11 h516909a_1006",
    "jupyter_core 4.6.3 py37hc8dfbb8_1",
    "liblief 0.9.0 hf8a498c_1",
    "py-lief 0.9.0 py37he1b5a44_1",
    "traitlets 4.3.3 py37hc8dfbb8_1",
    "conda-package-handling 1.6.0 py37h8f50634_2",
    "patch 2.7.6 h14c3975_1001",
    "anaconda-client 1.7.2 py_0",
    "filelock 3.0.12 pyh9f0ad1d_0",
    "decorator 4.4.2 py_0",
    "curl 7.71.1 he644dc0_0",
    "requests 2.24.0 pyh9f0ad1d_0",
    "libxml2 2.9.10 h72b56ed_1",
    "python-dateutil 2.8.1 py_0",
    "urllib3 1.25.9 py_0",
    "zstd 1.4.4 h6597ccf_3",
    "ripgrep 12.1.1 h516909a_0",
    "beautifulsoup4 4.9.1 py37hc8dfbb8_0",
    "xz 5.2.5 h516909a_0",
    "pytz 2020.1 pyh9f0ad1d_0",
    "krb5 1.17.1 hfafb76e_1",
    "conda-build 3.19.2 py37hc8dfbb8_2",
    "pip 20.1.1 py_1",
    "conda-forge-ci-setup 2.8.4 py37hc8dfbb8_0",
    "conda-env 2.6.0 1",
    "click 7.1.2 pyh9f0ad1d_0"
  ],
  "summary": "Measure customer lifetime value in Python",
  "tags": []
}
''' > ${TMP}/lifetimes-0.11.1-py36h9f0ad1d_1/info/about.json

echo -e """# This file created by conda-build 3.19.2
# meta.yaml template originally from:
# /home/conda/recipe_root, last modified Mon Jul  6 12:16:32 2020
# ------------------------------------------------

package:
    name: lifetimes
    version: 0.11.1
source:
    sha256: 75862d86581e75f0c235d830590bea0a9062222f2c9c390949f6432a3fa329b4
    url: https://pypi.io/packages/source/L/Lifetimes/Lifetimes-0.11.1.tar.gz
build:
    number: '1'
    script: '/home/conda/feedstock_root/build_artifacts/lifetimes_1594037875906/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_p/bin/python
        -m pip install . --no-deps --ignore-installed -vv '
    string: py36hc560c46_1
requirements:
    host:
        - _libgcc_mutex 0.1 conda_forge
        - _openmp_mutex 4.5 0_gnu
        - bzip2 1.0.8 h516909a_2
        - ca-certificates 2020.6.20 hecda079_0
        - certifi 2020.6.20 py36hc560c46_0
        - expat 2.2.9 he1b5a44_2
        - gdbm 1.18 h0a1914f_1
        - libffi 3.2.1 he1b5a44_1007
        - libgcc-ng 9.2.0 h24d8f2e_2
        - libgomp 9.2.0 h24d8f2e_2
        - libstdcxx-ng 9.2.0 hdf63c60_2
        - ncurses 6.1 hf484d3e_1002
        - openssl 1.1.1g h516909a_0
        - pip 20.1.1 py_1
        - pypy3.6 7.3.1 h3e02ecb_1
        - python 3.6.9 2_73_pypy
        - python_abi 3.6 1_pypy36_pp73
        - readline 8.0 hf8c457e_0
        - setuptools 49.1.0 py36hc560c46_0
        - sqlite 3.32.3 hcee41ef_0
        - tk 8.6.10 hed695b0_0
        - wheel 0.34.2 py_1
        - xz 5.2.5 h516909a_0
        - zlib 1.2.11 h516909a_1006
    run:
        - autograd >=1.2.0
        - dill >=0.2.6
        - numpy >=1.10.0
        - pandas >=0.24.0
        - pypy3.6 >=7.3.1
        - python >=3.6,<3.7.0a0
        - python_abi 3.6 *_pypy36_pp73
        - scipy >=1.0.0
        - setuptools
test:
    imports:
        - lifetimes
        - lifetimes.datasets
about:
    doc_url: https://lifetimes.readthedocs.io/en/latest/?badge=latest
    home: https://github.com/CamDavidsonPilon/lifetimes
    license: MIT
    license_family: MIT
    license_file: README.md
    summary: Measure customer lifetime value in Python
extra:
    copy_test_source_files: true
    final: true
    recipe-maintainers:
        - null
""" > ${TMP}/lifetimes-0.11.1-py36hc560c46_1/info/recipe/meta.yaml

cd $TMP

# Tar compress
tar -cvjSf conda-forge_linux-64_lifetimes-0.11.1-py36h9f0ad1d_1.tar.bz2 -C lifetimes-0.11.1-py36h9f0ad1d_1 .
tar -cvjSf conda-forge_linux-64_lifetimes-0.11.1-py36hc560c46_1.tar.bz2 -C lifetimes-0.11.1-py36hc560c46_1 .

# Move .tar.bz2 archives to a servable directory
mv *.tar.bz2 ../../$BASE_PATH

# Clean up removing tmp_dir
cd ../../
rm -r tmp_dir/
