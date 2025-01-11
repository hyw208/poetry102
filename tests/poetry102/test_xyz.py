import pytest 

def test_xyz():
    from poetry102.xyz import func
    assert func() == "xyz's func"

def test_abc():
    from other_package.abc import func
    print('hello')
    assert func() == "abc"

# # vs code default won't find the other_package.abc
# if __name__ == "__main__":
#     test_abc()