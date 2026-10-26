from functions.write_file import write_file

def test() -> None:
    # Test writing to a file
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Write result: {result}")

    # Test writing to a file outside the working directory
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Write result: {result}")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Write result: {result}")

if __name__ == "__main__":
    test()