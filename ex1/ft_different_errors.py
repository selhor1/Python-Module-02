def garden_operations(temp_str: str) -> None:
    if temp_str == "value":
        print("Testing ValueError...")
        try:
            int("abc")
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
    elif temp_str == "zero":
        print("Testing ZeroDivisionError...")
        try:
            10 / 0
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")
    elif temp_str == "file":
        print("Testing FileNotFoundError...")
        try:
            f = open("missing.txt")
            f.close()
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")
    elif temp_str == "key":
        print("Testing KeyError..")
        my_dict = {"rose": 1}
        try:
            _ = my_dict["missing_plant"]
        except KeyError as e:
            print(f"Caught KeyError: {e}\n")
    elif temp_str == "multiple":
        print("Testing multiple errors together...")
        my_dict = {"rose": 1}
        try:
            int("abc")
            10 / 0
            f = open("missing.txt")
            _ = my_dict["missing_plant"]
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    tests = ["value", "zero", "file", "key", "multiple"]
    for value in tests:
        garden_operations(value)
    print("All error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print(f"Caught unexpected error: {e}")
