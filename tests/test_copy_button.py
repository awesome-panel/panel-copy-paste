"""Test the CopyButton."""

import pandas as pd
import param
import polars as pl
import pytest

from panel_copy_paste import CopyButton


def test_create():
    """Can create the CopyButton."""
    value = "Hello World"

    button = CopyButton(value=value)
    assert button.button.clicks == 0


def test_copy():
    """Can copy with the CopyButton."""
    value = "Hello World"

    button = CopyButton(value=value)
    button.button.clicks += 1

    assert button._data == value


def test_transform_none():
    """Can copy None with the CopyButton."""
    value = None

    assert CopyButton._transform_value(value) == ""


def test_transform_str():
    """Can copy with the CopyButton."""
    value = "Hello World"

    assert CopyButton._transform_value(value) == value


@pytest.mark.parametrize(
    ["decimal_seperator", "expected"],
    [
        (None, "x\n1.1\n"),
        (".", "x\n1.1\n"),
        (",", "x\n1,1\n"),
    ],
)
def test_transform_pandas_dataframe(decimal_seperator, expected):
    """Can copy with the CopyButton."""
    value = pd.DataFrame({"x": [1.1]})

    assert CopyButton._transform_value(value, decimal_separator=decimal_seperator) == expected


@pytest.mark.parametrize(
    ["index", "expected"],
    [
        (True, "\tx\n0\t1.1\n"),
        (False, "x\n1.1\n"),
    ],
)
def test_transform_pandas_dataframe_index(index, expected):
    """Can copy with the CopyButton."""
    value = pd.DataFrame({"x": [1.1]})

    assert CopyButton._transform_value(value, index=index) == expected


@pytest.mark.parametrize(
    ["decimal_seperator", "expected"],
    [
        (None, "x\n1.1\n"),
        (".", "x\n1.1\n"),
        (",", "x\n1,1\n"),
    ],
)
def test_transform_polars_dataframe(decimal_seperator, expected):
    """Can transform Polars DataFrame."""
    value = pl.DataFrame({"x": [1.1]})
    assert CopyButton._transform_value(value, decimal_separator=decimal_seperator) == expected


def test_transform_callback():
    """Can transform callback."""

    def callback():
        return pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})

    assert CopyButton._transform_value(callback) == "x\ty\n1\ta\n2\tb\n"


def test_transform_parameter():
    """Can transform parameter."""

    class MyClass(param.Parameterized):
        value = param.Parameter()

    value = pl.DataFrame({"x": [1, 2], "y": ["a", "b"]})
    my_instance = MyClass(value=value)
    assert CopyButton._transform_value(my_instance.param.value) == "x\ty\n1\ta\n2\tb\n"


def test_transform_parameterized_with_value_parameter():
    """Can transform Parameterized with value parameter."""

    class MyClass(param.Parameterized):
        value = param.Parameter()

    value = pl.DataFrame({"x": [1, 2], "y": ["a", "b"]})
    my_instance = MyClass(value=value)
    assert CopyButton._transform_value(my_instance) == "x\ty\n1\ta\n2\tb\n"


def test_transform_parameterized_with_object_parameter():
    """Can transform Parameterized with value parameter."""

    class MyClass(param.Parameterized):
        object = param.Parameter()

    value = pl.DataFrame({"x": [1, 2], "y": ["a", "b"]})
    my_instance = MyClass(object=value)
    assert CopyButton._transform_value(my_instance) == "x\ty\n1\ta\n2\tb\n"
