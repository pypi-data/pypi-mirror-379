import sys
from .core import range_sum

def main():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print(f"Sum from {a} to {b}: {range_sum(a,b)}")
    except (IndexError, ValueError):
        print("Usage: RangeNumbersSumLibrary <start> <end>")

if __name__ == "__main__":
    main()
