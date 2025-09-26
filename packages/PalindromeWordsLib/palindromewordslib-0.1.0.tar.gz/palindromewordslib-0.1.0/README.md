# PalindromeWordsLib
مكتبة لاستخراج الكلمات المتناظرة (Palindrome) من نص.

## التثبيت
pip install PalindromeWordsLib

## CMD
palindromewordslib "madam racecar test"
# Palindrome words: ['madam', 'racecar']

## Python
from palindrome_words_lib import extract_palindrome_words
text = "madam racecar test"
print(extract_palindrome_words(text))  # ['madam', 'racecar']
