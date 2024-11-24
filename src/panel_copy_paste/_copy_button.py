import logging

import panel as pn
import param
from narwhals.dependencies import is_into_dataframe, is_pandas_dataframe, is_polars_dataframe
from narwhals.typing import IntoDataFrame

logger = logging.getLogger(__name__)


class CopyButton(pn.custom.JSComponent):
    value = param.Parameter(doc="""A String or DataFrame. Or a callback, Parameter or Parameterized object providing such types.""")
    button = pn.custom.Child(constant=True, doc="""A custom Button or ButtonIcon to use.""")

    _DEFAULT_BUTTON = pn.widgets.ButtonIcon(description="Copy to clip board.", icon="copy", active_icon="check", toggle_duration=1500)
    _data = param.Parameter(doc="""The value to be transferred to the clip board.""")

    _rename = {"value": None}
    _esm = """
    export function render({ model, el }) {
      const button = model.get_child("button")
      el.appendChild(button)

      model.on("_data", (e)=>{
        navigator.clipboard.writeText(model._data).then(function() {
            console.log('Writing to clipboard was successful!');
        }, function(err) {
            console.error('Could not write to clipboard: ', err);
        });
      })
    }
    """

    def __init__(self, **params):
        if "button" not in params:
            params["button"] = self._get_new_button()
        super().__init__(**params)

    @classmethod
    def _get_new_button(cls):
        return cls._DEFAULT_BUTTON.clone()

    @param.depends("button.clicks", watch=True)
    def _handle_clicks(self):
        self._data = self._transform_value(self.value)

    @staticmethod
    def _transform_frame(value: IntoDataFrame) -> str:
        if is_pandas_dataframe(value):
            return value.to_csv(sep="\t")
        if is_polars_dataframe(value):
            return value.write_csv(separator="\t")

        msg = f"Value of type '{type(value)} is not supported yet."
        raise ValueError(msg)

    @classmethod
    def _transform_value(cls, value, transform_func=None) -> str:
        if isinstance(value, param.Parameterized):
            if hasattr(value, "value"):
                return cls._transform_frame(value.value)
            elif hasattr(value, "object"):
                return cls._transform_frame(value.object)
        elif isinstance(value, param.Parameter):
            return cls._transform_value(value.rx.value)
        elif callable(value):
            return cls._transform_frame(value())

        if value is None:
            return ""
        if isinstance(value, str):
            return value
        if is_into_dataframe(value):
            return cls._transform_frame(value)

        msg = f"Value of type '{type(value)} is not supported yet."
        raise ValueError(msg)

    @classmethod
    def _create_test_app(cls):
        str_button = cls(value="Hello String World")
        import pandas as pd

        pandas_button = cls(value=pd.DataFrame({"x": [1, 2], "pandas": ["a", "b"]}), button=pn.widgets.Button(name="Copy Pandas", icon="copy"))
        import polars as pl

        polars_button = cls(
            value=pl.DataFrame({"x": [1, 2], "polars": ["a", "b"]}),
            button=pn.widgets.ButtonIcon(name="Copy Polars", icon="copy", active_icon="check", toggle_duration=1500),
        )

        text_area_input = pn.widgets.TextAreaInput(rows=10)
        return pn.Row(pn.Column(str_button, pandas_button, polars_button), text_area_input)


if pn.state.served:
    CopyButton._create_test_app().servable()
