"""Practice with dictionaries."""

__author__ = "730214639"

# Define your functions below


def invert(a: dict[str, str]) -> dict[str, str]:
    """Function that inverts a dictionary."""
    invert = {}
    for key, value in a.items():
        invert = {value: key for key, value in a.items()}
        if key == value in a:
            raise KeyError("keys MUST be unique")
    return invert


def favorite_color(a: dict[str, str]) -> str:
    """Function that returns a favorite color."""
    favorite: str = ""
    empty_dict: dict[str, int] = {}
    max: int = 0
    for item in a:
        if item not in empty_dict:
            empty_dict[a[item]] = 1
        else:
            empty_dict[a[item]] += 1
    for item in empty_dict:
        if empty_dict[item] > max:
            favorite = item
            max = empty_dict[favorite]
    return favorite


def count(a: list[str]) -> dict[str, int]:
    """Function that counts how many times an object appears in a list."""
    counter: dict[str, int] = {}
    for item in a:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1
    return counter 