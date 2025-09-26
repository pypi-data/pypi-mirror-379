import sys
from .core import extract_palindrome_words

def main():
    if len(sys.argv) < 2:
        print("Usage: PalindromeWordsLib <text>")
        return
    text = " ".join(sys.argv[1:])
    palindromes = extract_palindrome_words(text)
    print("Palindrome words:", palindromes)

if __name__ == "__main__":
    main()
