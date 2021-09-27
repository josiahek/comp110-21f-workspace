"""example of a function that processes a list."""

# define a function named contains
# we can give 2 arguments: needle value we're searching for in a haystack list


def main() -> None:
    names: list[str] = ["Josiah", "Sawyer"]
    print(contains("Josiah", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Retrun true if needle is found in haystack. false otherwise."""
    # loop through each indext in list
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            # test if item stored at index is equal to needle
            # return true if so
            return True
        i += 1
    # return false after testing each time
    return False


if __name__ == "__main__":
    main()