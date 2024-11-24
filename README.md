# ✨ panel-copy-paste

[![CI](https://img.shields.io/github/actions/workflow/status/awesome-panel/panel-copy-paste/ci.yml?style=flat-square&branch=main)](https://github.com/awesome-panel/panel-copy-paste/actions/workflows/ci.yml)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/panel-copy-paste?logoColor=white&logo=conda-forge&style=flat-square)](https://prefix.dev/channels/conda-forge/packages/panel-copy-paste)
[![pypi-version](https://img.shields.io/pypi/v/panel-copy-paste.svg?logo=pypi&logoColor=white&style=flat-square)](https://pypi.org/project/panel-copy-paste)
[![python-version](https://img.shields.io/pypi/pyversions/panel-copy-paste?logoColor=white&logo=python&style=flat-square)](https://pypi.org/project/panel-copy-paste)

Extends HoloViz Panel with copy-paste functionality.

## Features

- `CopyButton`: Enables you to copy Python objects to the clipboard.

## Installation

Install it via `pip`:

```bash
pip install panel-copy-paste
```

## Usage

To use the `CopyButton`:

```python
from panel_copy_paste import CopyButton

CopyButton(value="Hello World").servable()
```

## Supported Types

As `value` you can use any of the types below.

- `None`: Will copy as the empty string.
- `str`: Any String value
- `DataFrame`: Pandas and Polars dataframes will copy as a tab separated csv string.

More types can be supported. Please [create a Feature Request](https://github.com/awesome-panel/panel-copy-paste/issues).

In addition the below values will be resolved to above types

- `Parameterized`: Must have `.value` or `.object` attribute.
- `Parameter`:
- `Callback`:

## Development

```bash
git clone https://github.com/awesome-panel/panel-copy-paste
cd panel-copy-paste
```

For a simple setup use [`uv`](https://docs.astral.sh/uv/):

```bash
uv venv
source .venv/bin/activate # on linux. Similar commands for windows and osx
uv pip install -e .[dev]
pre-commit run install
pytest tests
```

For the full setup used by Github Actions use [`pixi`](https://pixi.sh):

```bash
pixi run pre-commit-install
pixi run postinstall
pixi run test
```

This repository is based on [copier-template-panel-extension](https://github.com/panel-extensions/copier-template-panel-extension).
To update to the latest template version run:

```bash
pixi exec --spec copier --spec ruamel.yaml -- copier update --defaults --trust
```

Note: `copier` will show `Conflict` for files with manual changes during an update. This is normal. As long as there are no merge conflict markers, all patches applied cleanly.

## ❤️ Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and passes all tests.
