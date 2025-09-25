# `cronian` developer documentation

If you're looking for user documentation, go [here](README.md).

## Development install

```shell
# Create a virtual environment, e.g. with
python -m venv .venv

# activate virtual environment
source .venv/bin/activate

# make sure to have a recent version of pip and setuptools
python -m pip install --upgrade pip setuptools

# (from the project root directory)
# install cronian as an editable package
python -m pip install --no-cache-dir --editable .
# install development dependencies
python -m pip install --no-cache-dir --editable .[dev]
```

Afterwards check that the install directory is present in the `PATH` environment variable.

## Running the tests

There are two ways to run tests.

The first way requires an activated virtual environment with the development tools installed:

```shell
pytest -v
```

The second is to use `tox`, which can be installed separately (e.g. with `pip install tox`), i.e.
not necessarily inside the virtual environment you use for installing `cronian`, but then builds the
necessary virtual environments itself by simply running:

```shell
tox
```

Testing with `tox` allows for keeping the testing environment separate from your development
environment. The development environment will typically accumulate (old) packages during development
that interfere with testing; this problem is avoided by testing with `tox`.

### Test coverage

In addition to just running the tests to see if they pass, they can be used for coverage statistics,
i.e. to determine how much of the package's code is actually executed during tests. In an activated
virtual environment with the development tools installed, inside the package directory, run:

```shell
coverage run
```

This runs tests and stores the result in a `.coverage` file.
To see the results on the command line, run

```shell
coverage report  # add the '-m' flag to indicate missed line numbers
```

Alternatively, you can call pytest to directly perform and report the coverage with

```shell
pytest --cov --cov-report   # add the 'term-missing' option to indicate missed line numbers
```

`coverage` can also generate output in HTML and other formats; see `coverage help` for more
information.


## Running linters locally

For linting and sorting imports we will use [ruff](https://beta.ruff.rs/docs/). Running the linters requires an 
activated virtual environment with the development tools installed.

```shell
# linter
ruff check .

# linter with automatic fixing
ruff check . --fix
```

To fix readability of your code style you can use [yapf](https://github.com/google/yapf).

You can enable automatic linting with `ruff` on commit by enabling the git hook from
`.githooks/pre-commit`, like so:

```shell
git config --local core.hooksPath .githooks
```

## Generating the API docs

```shell
cd docs
make html
```

The documentation will be in `docs/_build/html`

If you do not have `make` use

```shell
sphinx-build -b html docs docs/_build/html
```

To find undocumented Python objects run

```shell
cd docs
make coverage
cat _build/coverage/python.txt
```

To [test snippets](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html) in documentation run

```shell
cd docs
make doctest
```

## Versioning

Bumping the version across all files is done with [bump-my-version](https://github.com/callowayproject/bump-my-version), e.g.

```shell
bump-my-version bump major  # bumps from e.g. 0.3.2 to 1.0.0
bump-my-version bump minor  # bumps from e.g. 0.3.2 to 0.4.0
bump-my-version bump patch  # bumps from e.g. 0.3.2 to 0.3.3
```

To execute a dry run to see what changes will be made, for example to bump `minor`, run
```shell
bump-my-version bump minor --dry-run --verbose
```

## Making a release

This section describes how to make a release in 2 parts:

1. preparation
1. making a release on GitLab

### (1/2) Preparation

1. Update the <CHANGELOG.md> (don't forget to update links at bottom of page)
2. Verify that the information in [`CITATION.cff`](CITATION.cff) is correct.
3. Make sure the [version has been updated](#versioning).
4. Run the unit tests with `pytest -v`


### (2/2) GitLab

Don't forget to also make a [release on GitLab](https://gitlab.tudelft.nl/demoses/cronian/-/releases/new).
Once your release is ready, be sure to upload the new version to Zenodo too.


## Our style preferences

All files should be formatted using `ruff format`. While we may not agree with all its choices,
it is worth more to us that we don't have to worry about the formatting.

### Function docstring/documentation
```
def some_function(
      a: str,
      b: int,
      c: float,
      d: list[float],
      e: dict[str, list],
) -> tuple[float, float]:
      """Does something nice.

      Args:
           a: description of a
           b: description of b ...
               description of b continues
           c: ...
           d: ...
           e: ...

      Returns:
           The min and max values of something. (Note: Type hint not needed here)

      Raises:
           FasterThanLightError: If speed is greater than the speed of light.
      """
      code starts here
```
