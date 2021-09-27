"""List utility functions."""

__author__ = "730214639"


# TODO: Implement your functions here.
def all(haystack: list[int], needle: int) -> bool:
    """Function to answer question 1."""
    i: int = 0
    empty_list: list[int] = []
    if haystack == empty_list:
        return False
    while i < len(haystack):
        if haystack[i] != needle:
            return False
        i += 1
    return True


def is_equal(haystack2: list[int], needle2: list[int]) -> bool:
    """Function to answer question 2."""
    i: int = 0
    empty_list: list[int] = []
    if haystack2 == empty_list and needle2 == empty_list:
        return True
    if haystack2 == empty_list or needle2 == empty_list:
        return False
    if len(haystack2) != len(needle2):
        return False
    while i < len(haystack2) or i < len(needle2):
        if haystack2[i] != needle2[i]:
            return False
        i += 1
    return True
    

def max(input: list[int]) -> int:
    """Function to answer question 3.""" 
    i: int = 0
    j: int = 1
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max = input[i]
    while j < len(input):
        if max < input[j]:
            max = input[j]
        j += 1
    return max
    