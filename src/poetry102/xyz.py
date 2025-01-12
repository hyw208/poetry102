def func_xyz():
    from other_package.abc import func_abc
    return "xyz"

if __name__ == "__main__":
	print(func_xyz())