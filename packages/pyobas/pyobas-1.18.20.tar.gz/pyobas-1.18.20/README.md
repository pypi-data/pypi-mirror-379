# OpenBAS client for Python

[![Website](https://img.shields.io/badge/website-openbas.io-blue.svg)](https://openbas.io)
[![CircleCI](https://circleci.com/gh/OpenBAS-Platform/client-python.svg?style=shield)](https://circleci.com/gh/OpenBAS-Platform/client-python/tree/main)
[![readthedocs](https://readthedocs.org/projects/openbas-client-for-python/badge/?style=flat)](https://openbas-client-for-python.readthedocs.io/en/latest/)
[![GitHub release](https://img.shields.io/github/release/OpenBAS-Platform/client-python.svg)](https://github.com/OpenBAS-Platform/client-python/releases/latest)
[![Number of PyPI downloads](https://img.shields.io/pypi/dm/pyobas.svg)](https://pypi.python.org/pypi/pyobas/)
[![Slack Status](https://img.shields.io/badge/slack-3K%2B%20members-4A154B)](https://community.filigran.io)

The official OpenBAS Python client helps developers to use the OpenBAS API by providing easy to use methods and utils.
This client is also used by some OpenBAS components.

## Install

To install the latest Python client library, please use `pip`:

```bash
$ pip3 install pyobas
```

## Local development

```bash
# Fork the current repository, then clone your fork
$ git clone https://github.com/YOUR-USERNAME/client-python
$ cd client-python
$ git remote add upstream https://github.com/OpenBAS-Platform/client-python.git
# Create a branch for your feature/fix
$ git checkout -b [branch-name]
# Create a virtualenv
$ python3 -m venv .venv
$ source .venv/bin/activate
# Install the client-python and dependencies for the development and the documentation
$ python3 -m pip install -e .[dev,doc]
# Set up the git hook scripts
$ pre-commit install
# Create your feature/fix
# Create tests for your changes
$ python -m unittest
# Push you feature/fix on Github
$ git add [file(s)]
$ git commit -m "[descriptive message]"
$ git push origin [branch-name]
# Open a pull request
```

### Install the package locally

```bash
$ pip install -e .
```

## Documentation

### Client usage

To learn about how to use the OpenBAS Python client and read some examples and cases, refer to [the client documentation](https://openbas-client-for-python.readthedocs.io/en/latest/client_usage/getting_started.html).

### API reference

To learn about the methods available for executing queries and retrieving their answers, refer to [the client API Reference](https://openbas-client-for-python.readthedocs.io/en/latest/pyobas/pyobas.html).

## Tests

The standard `unittest` library is used for running the tests.

```bash
$ python -m unittest
```

## Code Coverage

To run the tests and generate a code coverage report:

```bash
pytest --cov=. tests/
```

## About

OpenBAS is a product designed and developed by the company [Filigran](https://filigran.io).

<a href="https://filigran.io" alt="Filigran"><img src="https://github.com/OpenBAS-Platform/openbas/raw/master/.github/img/logo_filigran.png" width="300" /></a>
