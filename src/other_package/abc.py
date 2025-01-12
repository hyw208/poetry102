def func_abc():
    from poetry102.xyz import func_xyz
    from other_package.abc import func_abc
    return "abc"

if __name__ == "__main__":
	print(func_abc())