"""Finding duplicate letters in a word."""

__author__ = "730214639"

user_str: str = input("Enter a word: ")
dupe: bool = False
i: int = 0 

while i < len(user_str):
    char = user_str[i]
    j: int = i + 1
    d: int = i + 1
    while j < len(user_str):
        if char == user_str[j]:
            print("Found duplicate:", not dupe)
            j = j + 1
            d = d + 1
        else:
            d = j
            j = j + 1 
    if d == len(user_str): 
        print("Found duplicate:", dupe)
        d = d + 1
    i = i + 1