import pytest
from khalil_zaidi_calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5

def test_divide():
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    try:
        calc.divide(5, 0)
    except ZeroDivisionError:
        assert True

def test_power():
    assert calc.power(2, 3) == 8

def test_sqrt():
    assert calc.sqrt(16) == 4

def test_average():
    assert calc.average([1, 2, 3, 4]) == 2.5
