import sys
from .core import char_frequency

def main():
    if len(sys.argv) < 2:
        print("Usage: CharFrequencyLib <text>")
        return
    text = " ".join(sys.argv[1:])
    freq = char_frequency(text)
    for char, count in freq.items():
        print(f"'{char}': {count}")

if __name__ == "__main__":
    main()
