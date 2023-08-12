"""File manipulation: Write a program that reads the contents of a file and counts the number of occurrences of each
word in it.
"""
import string
from collections import defaultdict

if __name__ == '__main__':
    with open("words.txt", "r") as file:
        content = file.read()
        # 去除标点符号
        translator = str.maketrans('', '', string.punctuation)
        content_without_punctuations = content.translate(translator)
        words = [word.lower() for word in content_without_punctuations.split()]
        words_dict = defaultdict(int)
        for word in words:
            words_dict[word] += 1
        print(words_dict)

