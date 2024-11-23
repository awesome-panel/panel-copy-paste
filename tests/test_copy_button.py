"""Test the CopyButton."""

from panel_copy_paste import CopyButton


def test_copy_button():
    """Test the CopyButton."""
    value = "Hello World"

    button = CopyButton(value=value)
    button._clicks += 1

    assert button._data == value
