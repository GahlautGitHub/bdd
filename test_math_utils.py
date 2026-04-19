from math_utils import add, substract, divide
import pytest


def test_add():
    assert add(2, 3) == 5


def test_substract():
    assert substract(2, 3) == -1


def test_divide():
    assert divide(6, 3) == 2


def test_divide_byZero():
    with pytest.raises(ValueError):
        divide(10, 0)
