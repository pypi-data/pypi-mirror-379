import sys
from .core import count_words 

def main():
    if len(sys.argv) < 2:
        print("Usage: WordCountLibRS <text>")
        return
    text = " ".join(sys.argv[1:])
    print(f"Word count: {count_words(text)}") 

if __name__ == "__main__":
    main()
