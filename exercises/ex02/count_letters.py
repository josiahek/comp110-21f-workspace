"""Counting letters in a string."""

__author__ = "730214639"


# Begin your solution here...
user_letter: str = input("What letter do you want to search for?: ")
user_word: str = input("Enter a word: ")

i: int = 0
count: int = 0

while i < len(user_word):
    if user_word[i] == user_letter:
        count = count + 1
        i = i + 1
    else:
        i = i + 1
print("Count:", count)