import pytest 

def test_xyz():
    from poetry102.xyz import func
    assert func() == "xyz's func"