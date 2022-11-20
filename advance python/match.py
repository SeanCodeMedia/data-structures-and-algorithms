from enum import Enum


class Colors(Enum):
    RED = "red"
    BLUE = "blue"
    WHITE = "White"
    GREEN = "green"


def find_match(phrase):
    match phrase:

        case "Hello":
            print("world")
        case "bye":
            print("bye world")

        case _:
            print("No Match found :(")


# find_match("")


# match with gard

def find_match(color):
    match color:
        case Colors.RED:
            print("Red")
        case Colors.BLUE if color == Colors.BLUE:
            print("Blue")
        case Colors.WHITE:
            print("White")
        case _:
            print("No Match found :(")

# find_match(Colors.BLUE)


def find_match(color):
    match color:
        case Colors.RED | Colors.BLUE | Colors.GREEN:
            print("RGB")
        case _:
            print("No Match found :(")


find_match(Colors.BLUE)