from functions.run_python_file import run_python_file

def test() -> None:
    # Test running a Python file
    result = run_python_file("calculator", "main.py")
    print(f"Run result: {result}")

    # Test running a Python a simple mathematical operation
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Run result: {result}")

    # Test running a calculator's tests
    result = run_python_file("calculator", "tests.py")
    print(f"Run result: {result}")

    # Test should return an error because the file does not exist
    result = run_python_file("calculator", "../main.py")
    print(f"Run result: {result}")

    # Test should return an error because the file is not a Python file
    result = run_python_file("calculator", "nonexistent.py")
    print(f"Run result: {result}")

    # Test should return an error because the file is not a Python file
    result = run_python_file("calculator", "lorem.txt")
    print(f"Run result: {result}")


if __name__ == "__main__":
    test()