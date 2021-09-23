"""choose your own adventure project."""

__author__ = "730214639"
from random import randint
i: int = 0
points: int = 1
player: str = ""
NAMED_CONSTANT: str = '\U0001F92A'
MONEY: str = '\U0001F4B0'
THINK: str = '\U0001F914'
PARTY: str = '\U0001F389'


def main() -> None:
    """Begins the game."""
    greet()
    global points
    choice: str = input("How much would you like to inflate the ballon? Respond using N, L, M, or H for intensity. ")
    if choice == "N" or choice == "n":
        print(f"{player}, you chose to not inflate. Thank you for playing the game. You ended with ${points}. {NAMED_CONSTANT} ")
        loop: str = input(f"Would you like to play again {player}? Enter Y or N ")
        if loop == "Y" or loop == "y":
            main()
        elif loop == "N" or loop == "n":
            print(f"Hope you had fun! {PARTY}{PARTY}")
    elif choice == "L" or choice == "l":
        lightly()
    elif choice == "M" or choice == "m":
        medium()
    elif choice == "H" or choice == "h":
        high()
    

def greet() -> None:
    """Greets the player. Provides background info."""
    global player
    name: str = input("What is your name? ")
    player = name
    print(f"Hello {player}, You start with $1. Each time you inflate a ballon you can gain $1, $2, or $4.")
    print("Each round you can choose to not inflate the balloon or inflate (lightly ($1), moderately ($2), heavily ($4)).")
    print("Your goal is to end up with the most money without bursting the balloon.")
    print("When the balloon pops is completely randomized, but is more likely if inflated with a higher intensity.")
    print("You cannot inflate with the same intensity consecutively.")


def lightly() -> None:
    """Adventure path 1."""
    global points
    burst: int = 5
    lightly: int = int(randint(1, 5))
    if lightly < burst:
        points = points + 1
        print(f"{player}, the balloon didn't burst. You have ${points}.")
        again: str = input("Would you like to inflate again? (N, M, H). ")
        if again == "N" or again == "n":
            print(f"{player}, you chose to not inflate. Thank you for playing the game. You ended with ${points}. Were you risk-taking or risk-averse? {THINK}{THINK}")
        elif again == "M" or again == "m":
            medium()
        elif again == "H" or again == "h":
            high()
    if lightly == burst:
        print(f"The balloon burst. {player}, you ended with ${points}. {MONEY}{MONEY}{MONEY}")
        loop: str = input(f"Would you like to play again {player}? Enter Y or N ")
        if loop == "Y" or loop == "y":
            main()
        elif loop == "N" or loop == "n":
            print(f"Hope you had fun! {PARTY}{PARTY}")


def medium() -> None:
    """Adventure path 2."""
    global points
    burst: int = 4
    medium: int = int(randint(1, 4))
    if medium < burst:
        points = points + 2
        print(f"{player}, the balloon didn't burst. You have ${points}")
        again: str = str(input("Would you like to inflate again? (N, L, H). "))
        if again == "N" or again == "n":
            print(f"{player}, you chose to not inflate. Thank you for playing the game. You ended with ${points}. Were you risk-taking or risk-averse? {THINK}{THINK}")
        elif again == "L" or again == "l":
            lightly()
        elif again == "H" or again == "h":
            high()
    if medium == burst:
        print(f"The balloon burst. {player}, you ended with ${points}. {MONEY}{MONEY}{MONEY}")
        loop: str = input(f"Would you like to play again {player}? Enter Y or N ")
        if loop == "Y" or loop == "y":
            main()
        elif loop == "N" or loop == "n":
            print(f"Hope you had fun! {PARTY}{PARTY}")


def high() -> None:
    """Adventure path 3."""
    global points
    burst: int = 3
    high: int = int(randint(1, 3))
    if high < burst:
        points = points + 4
        print(f"{player}, the balloon didn't burst. You have ${points}")
        again: str = str(input("Would you like to inflate again? (N, L, M). "))
        if again == "N" or again == "n":
            print(f"You chose to not inflate. Thank you for playing the game. You ended with ${points}. Were you risk-taking or risk-averse? {THINK}{THINK}")
        elif again == "L" or again == 'l':
            lightly()
        elif again == "M" or again == "m":
            medium()
    if high == burst:
        print(f"The balloon burst. {player}, you ended with ${points}. {MONEY}{MONEY}{MONEY}")
        loop: str = input(f"Would you like to play again {player}? Enter Y or N ")
        if loop == "Y" or loop == "y":
            main()
        elif loop == "N" or loop == "n":
            print(f"Hope you had fun! {PARTY}{PARTY}")


if __name__ == "__main__":
    main()