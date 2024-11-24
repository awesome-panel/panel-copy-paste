# Copy Button

The `CopyButton` can be used to copy-paste any **string `value`**:

```{.python pycafe-embed pycafe-embed-height="100px" hl_lines="3"}
from panel_copy_paste import CopyButton

CopyButton(value="Hello World").servable()
```

Try clicking the `CopyButton` above and pasting the value into your editor.

You can also provide a **Pandas or Polars `DataFrame`** `value`:

```{.python pycafe-link extra-requirements="polars" hl_lines="4-5"}
from panel_copy_paste import CopyButton
import polars as pl

dataframe = pl.DataFrame({"Hello": [1,2], "World": ["a", "b"]})
CopyButton(value=dataframe).servable()
```

You can also provide a **`callback` (function), `Parameter`, or `Parameterized`** object:

```{.python pycafe-link extra-requirements="pandas" hl_lines="7-8"}
import panel as pn
import pandas as pd
from panel_copy_paste import CopyButton

pn.extension("tabulator")

widget = pn.widgets.Tabulator(pd.DataFrame({"Hello": [1, 2], "World": ["a", "b"]}))
button = CopyButton(value=widget)

pn.Column(button, widget).servable()
```

If you want a **custom `button`**, it's also possible:

```{.python pycafe-link hl_lines="3-4"}
import panel as pn
from panel_copy_paste import CopyButton

button = pn.widgets.Button(name="Copy Hello World", icon="copy", button_type="primary", button_style="outline")
CopyButton(value="Hello World", button=button).servable()
```
