import sys
from reader import Reader


def main(file):
    reader = Reader(file=file)
    reader.read()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = input("Please Enter Path to File: ")
    main(file_name)