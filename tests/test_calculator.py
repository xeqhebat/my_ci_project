import pytest
from my_ci_project.calculator import add, divide, is_even

#сложение
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0

#деление
def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="На ноль делить нельзя"):
        divide(10, 0)

#четность
def test_is_even():
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(0) == True
    assert is_even(1) == False
    assert is_even(7) == False
    assert is_even(-2) == True
