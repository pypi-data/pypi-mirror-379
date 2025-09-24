# `ocpiupdate` - An updater for OpenCPI projects

[![pypi](https://img.shields.io/pypi/v/ocpiupdate)](https://pypi.org/project/ocpiupdate/)
[![release](https://gitlab.com/dawalters/ocpiupdate/-/badges/release.svg)](https://gitlab.com/dawalters/ocpiupdate/-/releases)
[![gitlab](https://gitlab.com/dawalters/ocpiupdate/badges/develop/pipeline.svg)](https://gitlab.com/dawalters/ocpiupdate/-/pipelines?page=1&scope=all&ref=develop)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![codecov](https://codecov.io/gitlab/dawalters/ocpiupdate/branch/develop/graph/badge.svg)](https://codecov.io/gitlab/dawalters/ocpiupdate)

`ocpiupdate` updates OpenCPI Projects to use style associated with newer
versions of OpenCPI.

For example:

- Using `<worker>-<model>.xml` for the Worker Description files, instead of
  `<worker>.xml`.
- Using `<component>.comp/<component>-comp.xml` for Component Specification
  files instead of `specs/<component>[-_]spec.xml`.
- Using `xml` files instead of `Makefile`s.

## Dependencies

This library requires Python 3.12 or newer. This means it doesn't support the
default system `python3` install on Ubuntu 20.04 or Ubuntu 22.04.

If you use a system with Python 3.11 or older, you need to either:

- Install a newer `python3` just for this library.
    - I'd recommend using a tool like [`uv`](https://docs.astral.sh/uv).
- Download and run the containerised version.

## Installation

### `pip`

You can install the latest release from [PyPi](https://pypi.org/project/ocpiupdate):

```bash
pip install ocpiupdate
```

Or, you can install this repository directly:

```bash
# Installs `develop` branch
pip install git+https://gitlab.com/dawalters/ocpiupdate

# Installs `v0.6.3` tag
pip install git+https://gitlab.com/dawalters/ocpiupdate@v0.6.3
```

### `docker` or `podman`

A `Dockerfile` is available that builds a container that can run `ocpiupdate`.

You can download prebuilt containers from the
[Gitlab Container Registry](https://gitlab.com/dawalters/ocpiupdate/container_registry).
This happens automatically when running a registry image without a local copy.

See [`scripts/ocpiupdate.sh`](https://gitlab.com/dawalters/ocpiupdate/-/tree/develop/scripts/ocpiupdate.sh)
for a script that allows running the `ocpiupdate:latest` container over more
than one project.

To download and use this script:

```bash
# If you want to keep a local copy of the script
curl -o ocpiupdate.sh https://gitlab.com/dawalters/ocpiupdate/-/raw/develop/scripts/ocpiupdate.sh
source ocpiupdate.sh

# If you don't want to keep a local copy of the script
source <(curl -s https://gitlab.com/dawalters/ocpiupdate/-/raw/develop/scripts/ocpiupdate.sh)
```

You can then use the terminal command `ocpiupdate` in exactly the same way as
the python script.

If you have built a local version of the container, then `ocpiupdate.sh` will
use that. Otherwise, it will download the container from the remote registry.

### Source tarball

You can download source releases from the
[Gitlab Releases page](https://gitlab.com/dawalters/ocpiupdate/-/releases).

## Configuration

The various functions that `ocpiupdate` performs are called `actions`.

You can view all available `actions`:

```bash
ocpiupdate --actions
```

```console
rename_hdl_owds_to_hyphen_hdl
rename_rcc_owds_to_hyphen_rcc
rename_spec_to_comp_except_project
rename_protocol_to_prot
rename_underscore_prot_to_hyphen_prot
translate_applications_from_makefile_to_xml
translate_hdl_adapters_from_makefile_to_xml
translate_hdl_assemblies_from_makefile_to_xml
translate_hdl_cards_from_makefile_to_xml
translate_hdl_device_from_makefile_to_xml
translate_hdl_platforms_from_makefile_to_xml
translate_hdl_primitives_from_makefile_to_xml
translate_hdl_worker_from_makefile_to_xml
translate_project_from_makefile_to_xml
translate_rcc_worker_from_makefile_to_xml
```

If you encounter issues with an `action`, you can disable it:

```bash
ocpiupdate \
    --skip-action rename_protocol_to_prot \
    --skip-action rename_underscore_prot_to_hyphen_prot \
    $project
```

## Disclaimer

This repository has no affiliation with OpenCPI.

The maintainer doesn't maintain OpenCPI.

The maintainer does not guarantee that `ocpiupdate` will result in a buildable
project. If you encounter difficulties, please open an issue.
