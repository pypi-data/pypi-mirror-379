import string

def is_palindrome(word: str) -> bool:
    """Check if a single word is palindrome"""
    word_clean = word.lower().translate(str.maketrans('', '', string.punctuation))
    return word_clean == word_clean[::-1]

def extract_palindrome_words(text: str) -> list:
    """Return list of palindrome words from text"""
    words = text.split()
    return [w for w in words if is_palindrome(w)]
