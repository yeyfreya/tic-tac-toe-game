import pytest

# recommended way to run pytest:
# python3 -m pytest test_factorial_pytest.py

from factorial import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_five():
    assert factorial(5) == 120

def test_factorial_ten():
    assert factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError) as exc_info:
        factorial(-1)
    assert str(exc_info.value) == "Factorial is undefined for negative numbers."