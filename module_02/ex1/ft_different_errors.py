#!/usr/bin/env python3

def garden_operations(error_type: str) -> None:
    """
    This function demonstrates handling different types of errors
    based on the input error_type.

    Parameters:
    error_type (str): A string indicating the type of error to be handled.
                      It can be "ValueError", "ZeroDivisionError",
                      "FileNotFoundError", "KeyError",
                      or any other string for unknown errors.
    Returns:  None
    """

    message: str = "Caught "
    if error_type == "ValueError":
        str_temp: str = "abc"
        try:
            print(int(str_temp))
        except ValueError:
            print(message + "ValueError: invalid literal for int()")
    elif error_type == "ZeroDivisionError":
        try:
            number = 10/0
            print(number)
        except ZeroDivisionError:
            print(message + "ZeroDivisionError: division by zero")
    elif error_type == "FileNotFoundError":
        try:
            file_name: str = "missing.txt"
            with open(file_name, "r") as f:
                f.read()
        except FileNotFoundError:
            print(message + f"FileNotFoundError: No such file '{file_name}'")
    elif error_type == "KeyError":
        try:
            d: dict = {"a": 1, "b": 2}
            target: str = "missing_plant"
            print(d[target])
        except KeyError as e:
            print(message + f"KeyError: {e}")
    else:
        try:
            raise Exception("Unknown error type")
        except Exception:
            print(message + "an error, but program continues!")


def test_error_types() -> None:
    """
    This function tests the garden_operations function
    with different error types.

    Returns: None
    """

    print("=== Garden Error Types Demo ===")
    error_types: list[str] = []
    error_types.extend([
        "ValueError", "ZeroDivisionError", "FileNotFoundError",
        "KeyError", "UnknownError"
    ])
    for error_type in error_types:
        if error_type == "UnknownError":
            print("\nTesting multiple errors together...")
        else:
            print(f"\nTesting {error_type}...")
        garden_operations(error_type)
    print("\nAll error types tested successfully!")        


if __name__ == "__main__":
    test_error_types()
