import pytest 
from poetry102.xyz import func_xyz
from other_package.abc import func_abc

def test_xyz():
    assert func_xyz() == "xyz"

def test_abc():
    assert func_abc() == "abc"