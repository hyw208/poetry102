import pytest 

def test_all_xyz():
    from poetry102.xyz import func
    assert func() == "xyz's func"

def test_all_abc():
    from other_package.abc import func
    assert func() == "abc"