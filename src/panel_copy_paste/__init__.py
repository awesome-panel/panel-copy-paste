"""`panel-copy-paste` provides features for copying to and pasting from the clipboard."""

import importlib.metadata
import warnings

from panel_copy_paste._copy_button import CopyButton
from panel_copy_paste._paste_button import PasteButton
from panel_copy_paste._paste_button import PasteToDataFrameButton

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError as e:  # pragma: no cover
    warnings.warn(f"Could not determine version of {__name__}\n{e!s}", stacklevel=2)
    __version__ = "unknown"

__all__ = ["CopyButton", "PasteButton", "PasteToDataFrameButton"]  # <- IMPORTANT FOR DOCS: fill with imports
