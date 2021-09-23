"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

user_input: int = int(input("Depth: "))
i: int = 0
tree: str = ""

if user_input <= 0:
    ""
else:
    while i < user_input:
        count: int = 0 
        if count < user_input:
            i = i + 1
            count = count + 1
            tree = str(TREE) + tree
        print(tree)
