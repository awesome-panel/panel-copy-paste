import logging

import panel as pn
import param
from narwhals.dependencies import is_into_dataframe
from narwhals.dependencies import is_pandas_dataframe
from narwhals.dependencies import is_polars_dataframe
from narwhals.typing import IntoDataFrame

logger = logging.getLogger(__name__)


class CopyButton(pn.custom.JSComponent):
    """
    A custom Panel widget to copy a value to the clipboard.

    Currently supports copying strings and DataFrames.

    Examples
    --------
    >>> from panel_copy_paste import CopyButton
    >>> CopyButton(value="Hello World").servable()

    """

    value = param.Parameter(doc="""A String or DataFrame. Or a callback, Parameter or Parameterized object providing such types.""")
    button = pn.custom.Child(constant=True, doc="""An optional custom Button or ButtonIcon to use.""")

    decimal_separator = param.Selector(
        default=None,
        objects=[None, ".", ","],
        doc="""The decimal symbol used when transforming a DataFrame. If not provided set to the decimal symbol of the client.""",
    )
    index = param.Boolean(default=False, doc="""Whether to include the index when copying a Pandas DataFrame.""")

    _DEFAULT_BUTTON = pn.widgets.ButtonIcon(description="Copy to clip board.", icon="copy", active_icon="check", toggle_duration=1500)
    _data = param.Parameter(doc="""The value to be transferred to the clip board.""")

    _rename = {"value": None, "index": None}
    _esm = """
    function getDecimalSeparator(locale) {
        const numberWithDecimalSeparator = 1.1;
        return Intl.NumberFormat(locale)
            .formatToParts(numberWithDecimalSeparator)
            .find(part => part.type === 'decimal')
            .value;
    }

    export function render({ model, el }) {
      const button = model.get_child("button")
      el.appendChild(button)

      if (model.decimal_separator === null) {
        model.decimal_separator = getDecimalSeparator();
      }

      model.on("_data", (e)=>{
        navigator.clipboard.writeText(model._data).then(function() { }, function(err) {
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
        self._data = self._transform_value(self.value, decimal_separator=self.decimal_separator)

    @staticmethod
    def _transform_frame(value: IntoDataFrame, index=False, decimal_separator=None) -> str:
        if decimal_separator not in [".", ","]:
            decimal_separator = "."

        if is_pandas_dataframe(value):
            return value.to_csv(sep="\t", decimal=decimal_separator, index=index)
        if is_polars_dataframe(value):
            # Polars does not support ",": https://github.com/pola-rs/polars/issues/19963
            # This assumes pandas and pyarrow is installed
            if decimal_separator == ",":
                return value.to_pandas().to_csv(sep="\t", decimal=decimal_separator, index=False)
            return value.write_csv(separator="\t")

        msg = f"Value of type '{type(value)} is not supported yet."
        raise ValueError(msg)

    @classmethod
    def _transform_value(cls, value, transform_func=None, index=False, decimal_separator=None) -> str:
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
            return cls._transform_frame(value, index=index, decimal_separator=decimal_separator)

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
