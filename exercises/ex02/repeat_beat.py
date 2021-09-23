"""Repeating a beat in a loop."""

__author__ = "730214639"


# Begin your solution here...
user_str: str = input("What beat do you want me to repeat? ")
i: int = 0
beat: str = ""

times_rep: int = int(input("How many times do you want me to repeat it? "))

if times_rep <= 0:
    print("No beat...")
else:
    while i < times_rep:
        count: int = 0
        while count < times_rep:
            i = i + 1
            count = count + 1
            beat = " " + user_str + beat
        if count == times_rep:
            print(beat)