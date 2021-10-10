"""List utility functions part 2."""

__author__ = "730214639"

# Define your functions below


def only_evens(haystack: list[int]) -> list[int]:
    """Function that returns only evens."""
    i: int = 0
    even_list: list = []
    while i < len(haystack):
        if haystack[i] % 2 == 0:
            even_list.append(haystack[i]) 
            i += 1
        else:
            i += 1
    return even_list


def sub(haystack2: list[int], start_index: int, end_index: int) -> list[int]:
    """Function that returns a subset of function."""
    i: int = 0
    empty_list: list = []
    returned_list: list = haystack2[start_index:end_index]
    if start_index < 0:
        start_index = haystack2[i]
    if start_index > len(haystack2) or end_index <= 0:
        return empty_list
    if haystack2 == empty_list or len(haystack2) == 0:
        return empty_list
    if end_index > len(haystack2):
        end_index = haystack2[len(haystack2) - 1]
    return returned_list


def concat(haystack3: list[int], haystack4: list[int]) -> list[int]:
    """Function that returns two functions added together."""
    return haystack3 + haystack4