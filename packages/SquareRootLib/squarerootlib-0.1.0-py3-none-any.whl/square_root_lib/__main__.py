import sys
from .core import sqrt_number

def main():
    try:
        number = float(sys.argv[1])
        print(f"Square root: {sqrt_number(number)}")
    except (IndexError, ValueError) as e:
        print("Error:", e)
        print("Usage: SquareRootLib <number>")

if __name__ == "__main__":
    main()