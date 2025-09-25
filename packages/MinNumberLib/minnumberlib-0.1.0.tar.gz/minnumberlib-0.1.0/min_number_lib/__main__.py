
import sys
from .core import find_min

def main():
    try:
        numbers = [float(x) for x in sys.argv[1:]]
        print(f"Smallest number: {find_min(numbers)}")
    except ValueError as e:
        print("Error:", e)
        print("Usage: MinNumberLib <num1> <num2> ...")

if __name__ == "__main__":
    main()
