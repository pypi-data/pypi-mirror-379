# Python Commons IP

## Introduction
This repository provides a Python interface to the Commons IP validator.

## Usage
```python
import py_commons_ip
succes, report = py_commons_ip.validate("/path/to/unzipped/zip")
```

## Building

Fetch the commons-ip submodule.

```sh
git submodule update --init --remote
```

Use the Makefile to build the JAR file. This requires a Java runtime and Maven.

```sh
make
```

The JAR file will be copied to `py_commons_ip/resources`.

## Release

Bump the version in `pyproject.toml` and add a matching tag `vX.Y.Z` to the commit to start the CI/CD.