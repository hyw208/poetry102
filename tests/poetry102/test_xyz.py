import pytest 

def test_xyz():
    from poetry102.xyz import func_xyz
    from other_package.abc import func_abc
    assert func_xyz() == "xyz"