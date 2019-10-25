# Docstringsについて
def example_func(param1, param2):
        """Example function with documented in the docstrings
        Args:
            param1: (int):The first parameter.
            param2: (str):The second parameter.
        Returns:
            bool: The return value. True for success, false otherwise.
        """
        print(param1)
        print(param2)
        return True

#以下どちらでも関数の説明を表示する事が出来る
print(example_func.__doc__)
help(example_func)