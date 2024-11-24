"""We can paste csv data into a Tabulator widget."""

import pandas as pd
import panel as pn

from panel_copy_paste import PasteToDataFrameButton


def test_paste_csv_input():
    """We can paste csv data into a Tabulator widget."""
    # When
    target = pn.widgets.Tabulator()
    widget = PasteToDataFrameButton(target=target)
    # Then
    assert not widget.value
    assert not target.value
    # When
    widget.data = """1\t2\t3\t4"""
    # Then
    expected = pd.DataFrame([{0: 1, 1: 2, 2: 3, 3: 4}])
    pd.testing.assert_frame_equal(widget.value, expected)
    pd.testing.assert_frame_equal(widget.value, target.value)
