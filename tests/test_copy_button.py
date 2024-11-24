"""Test the CopyButton."""

import pandas as pd
import param
import polars as pl

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


def test_transform_pandas_dataframe():
    """Can copy with the CopyButton."""
    value = pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})

    assert CopyButton._transform_value(value) == "\tx\ty\n0\t1\ta\n1\t2\tb\n"


def test_transform_polars_dataframe():
    """Can transform Polars DataFrame."""
    value = pl.DataFrame({"x": [1, 2], "y": ["a", "b"]})
    assert CopyButton._transform_value(value) == "x\ty\n1\ta\n2\tb\n"


def test_transform_callback():
    """Can transform callback."""

    def callback():
        return pd.DataFrame({"x": [1, 2], "y": ["a", "b"]})

    assert CopyButton._transform_value(callback) == "\tx\ty\n0\t1\ta\n1\t2\tb\n"


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
