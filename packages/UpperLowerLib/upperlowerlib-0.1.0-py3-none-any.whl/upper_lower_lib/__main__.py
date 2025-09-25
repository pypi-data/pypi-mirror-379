import sys
from .core import to_upper, to_lower 

def main():
    if len(sys.argv) < 3:
        print("Usage: UpperLowerLib <upper/lower> <text>")
        return
    command = sys.argv[1].lower()
    text = " ".join(sys.argv[2:])
    if command == "upper":
        print(to_upper(text))
    elif command == "lower":
        print(to_lower(text))
    else:
        print("Command must be 'upper' or 'lower'") 

if __name__ == "__main__":
    main()
