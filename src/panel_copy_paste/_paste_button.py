import logging
from io import StringIO
from typing import TYPE_CHECKING

import panel as pn
import param

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    import pandas as pd


def do_nothing(self, data: str) -> str:
    """Return the data."""
    return data


def read_csv(self, data: str) -> "pd.DataFrame":
    """Return the data as a DataFrame."""
    import pandas as pd

    if not data:
        return pd.DataFrame()
    return pd.read_csv(StringIO(data), sep="\t", header=None)


class PasteButtonBase(pn.custom.JSComponent):
    """A custom Panel widget to paste a value from the clipboard onto an optional target."""

    data = param.String(default="", doc="""The string value transferred from the clip board.""")
    button = pn.custom.Child(constant=True, doc="""A custom Button or ButtonIcon to use.""")
    target = param.Parameter(
        doc="""If a widget its value is set to value when it changes. If a Pane its object will be
        set to the value. If a callable the callable will be executed on the value.""",
        allow_refs=False,
    )

    transform_func = do_nothing
    _DEFAULT_BUTTON = pn.widgets.ButtonIcon(description="Paste from clipboard.", icon="clipboard", active_icon="check", toggle_duration=1500)

    _rename = {"value": None, "target": None}

    _esm = """
    export function render({ model, el }) {
      const button = model.get_child("button")
      el.appendChild(button)

      button.addEventListener('click', (event) => {
            navigator.clipboard.readText()
            .then(pastedData => {
                if (model.data==pastedData){
                    model.data=pastedData + " ";
                } else {
                    model.data = pastedData;
                }
            })

        });
    }
    """

    def __init__(self, **params):
        if "button" not in params:
            params["button"] = self._get_new_button()
        self.transform_func = params.pop("transform_func", self.transform_func)  # type: ignore[method-assign]
        super().__init__(**params)

    @classmethod
    def _get_new_button(cls):
        return cls._DEFAULT_BUTTON.clone()

    @param.depends("data", watch=True)
    def _handle_data(self):
        self.value = self.transform_func(self.data)
        if self.target:
            self._set_target_value(self.target, self.value)

    @staticmethod
    def _set_target_value(target, value):
        if callable(target):
            target(value)
        elif hasattr(target, "object"):
            target.object = value
        elif hasattr(target, "value"):
            target.value = value
        else:
            msg = f"Target of type '{type(target)}' is not supported."
            logger.error(msg)


class PasteButton(PasteButtonBase):
    value = param.String(default="", doc="""The value from the clip board as a string.""")

    transform_func = do_nothing


class PasteToDataFrameButton(PasteButtonBase):
    value = param.DataFrame(doc="""The value from the clip board as a Pandas DataFrame.""")

    transform_func = read_csv
