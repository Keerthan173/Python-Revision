from my_math import add
def test_add_positive():
    assert add(2,3)==5
def test_add_negative():
    assert add(2,3)==1
    
import pytest
from my_math import divide
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)
def test_divide_mormal():
    assert divide(10,2)==5