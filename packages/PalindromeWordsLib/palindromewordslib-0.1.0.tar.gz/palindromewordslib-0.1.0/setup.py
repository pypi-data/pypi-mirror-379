from setuptools import setup, find_packages

setup(
    name="PalindromeWordsLib",
    version="0.1.0",
    description="Extract palindrome words from text",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Elaf Jamal Omar",
    author_email="o25635635@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={"console_scripts": ["palindromewordslib=palindrome_words_lib.__main__:main"]},
)
