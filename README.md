# ✨ panel-copy-paste

[![CI](https://img.shields.io/github/actions/workflow/status/awesome-panel/panel-copy-paste/ci.yml?style=flat-square&branch=main)](https://github.com/awesome-panel/panel-copy-paste/actions/workflows/ci.yml)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/panel-copy-paste?logoColor=white&logo=conda-forge&style=flat-square)](https://prefix.dev/channels/conda-forge/packages/panel-copy-paste)
[![pypi-version](https://img.shields.io/pypi/v/panel-copy-paste.svg?logo=pypi&logoColor=white&style=flat-square)](https://pypi.org/project/panel-copy-paste)
[![python-version](https://img.shields.io/pypi/pyversions/panel-copy-paste?logoColor=white&logo=python&style=flat-square)](https://pypi.org/project/panel-copy-paste)
[![py.cafe](https://py.cafe/badge.svg)](https://py.cafe/awesome.panel.org/panel-copy-paste)

Extends HoloViz Panel with copy-paste functionality.

[![Copy-Paste Reference App](https://raw.githubusercontent.com/awesome-panel/panel-copy-paste/refs/heads/main/docs/assets/panel-copy-paste.gif)](https://py.cafe/awesome.panel.org/panel-copy-paste)

Copy-paste to and from your data apps as well as external applications like Excel.

## Features

- `CopyButton`: Enables you to copy Python objects to the clipboard.
- `PasteButton`: Enables you to paste strings from the clipboard.
- `PasteToDataFrameButton`: Enables you to paste strings from the clipboard into dataframe values.

## Pin your version!

This project is **in its early stages**, so if you find a version that suits your needs, it’s recommended to **pin your version**, as updates may introduce changes.

## Installation

Install it via `pip`:

```bash
pip install panel-copy-paste
```

## Usage

To use the `CopyButton`:

```python
import panel as pn
from panel_copy_paste import CopyButton

pn.extension("codeeditor")

editor = pn.widgets.CodeEditor()
button = CopyButton(value="Hello World")
pn.Column(button, editor).servable()
```

To use the `PasteButton`:

```python
import panel as pn
from panel_copy_paste import PasteButton

pn.extension("codeeditor")

editor = pn.widgets.CodeEditor()
button = PasteButton(target=editor)
pn.Column(button, editor).servable()
```

To use the `PasteToDataFrameButton`:

```python
import panel as pn
from panel_copy_paste import PasteToDataFrameButton

pn.extension("tabulator")

table = pn.widgets.Tabulator()
button = PasteToDataFrameButton(target=table)
pn.Column(button, table).servable()
```

For more examples check out the [documentation](https://awesome-panel.github.io/panel-copy-paste/).

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
