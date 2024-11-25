# Paste Buttons

## Paste to String

The `PasteButton` can be used to paste any **string `value`**:

```{.python pycafe-link pycafe-embed-height="100px" hl_lines="2,7"}
import panel as pn
from panel_copy_paste import PasteButton

pn.extension("codeeditor")

editor = pn.widgets.CodeEditor()
button = PasteButton(target=editor)
pn.Column(button, editor).servable()
```

If you want a **custom button**, it's also possible:

```{.python pycafe-link hl_lines="4-5"}
import panel as pn
from panel_copy_paste import PasteButton

pn.extension("codeeditor")

editor = pn.widgets.CodeEditor()
custom_button = pn.widgets.Button(name="Click here to Paste", icon="clipboard", button_type="primary", button_style="outline")
button = PasteButton(target=editor, button=custom_button)
pn.Column(button, editor).servable()
```

The `target` is optional and may be a *Widget or Pane like* `Parameterized` class, a `Parameter` or a callable (function). For example you can use a callable to lower case the string before pasting the value to a widget:

```{.python pycafe-link hl_lines="8,9,11"}
import panel as pn
from panel_copy_paste import PasteButton

pn.extension("codeeditor")

editor = pn.widgets.CodeEditor()

def lower_case(value):
    editor.value = value.lower()

button = PasteButton(target=lower_case)
pn.Column(button, editor).servable()
```

## Paste to DataFrame

The `PasteToDataFrameButton` can be used to **paste a *tab-separated* string from Excel** or another application into your data app:

```{.python pycafe-link extra-requirements="pandas" hl_lines="2,7"}
import panel as pn
from panel_copy_paste import PasteToDataFrameButton

pn.extension("tabulator")

table = pn.widgets.Tabulator()
button = PasteToDataFrameButton(target=table)
pn.Column(button, table).servable()
```
