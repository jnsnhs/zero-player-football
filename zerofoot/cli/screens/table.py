import os
from random import choice

NAMES = [
    "Münchener Löwen",
    "Preußen Dortmund",
    "FC Meiderich",
    "Eintr. Frankfurt",
    "VfB Stuttgart",
    "Hamburger SV",
    "FC Schalke 04",
    "1. FC Nürnberg",
    "Werder Bremen",
    "1. FC K'lautern",
    "Karlsruher SC",
    "Hannover 96",
    "Bayern München",
    "1. FC Köln",
    "Eintr. Braunschweig",
    "Hertha BSC",
    "Preußen Münster",
    "1. FC Saarbrücken"
]


def generate_clubs():
    clubs = []
    for name in NAMES:
        clubs.append({
            "rank_cur": 10,
            "rank_pre": 9,
            "change": choice(["-", "▲", "▼"]),
            "name": name,
            "games": 34,
            "win": 99,
            "draw": 99,
            "loss": 99,
            "goals_for": 100,
            "goals_against": 100,
            "goals_difference": 100,
            "points": 99
        })
    return clubs


def print_line(char="─", start="─", end="─"):
    print(start, end="")
    print(char * 78, end="")
    print(end, end="\n")


def print_table(clubs: list):
    # 80 columns x 25 lines
    SP = " "
    os.system("cls")
    print("Erste Liga", "2. Spieltag")
    print_line("─", "┌", "┐")
    print(f"│{SP*3}PL.{SP*7}VEREIN{SP*18}SP{SP*5}G  U  V{SP*4}TORE{SP*6}DIFF.  PKT   │")
    print_line("─", "├", "┤")
    for club in clubs:
        print(
            f"│   "
            f"{club["rank_cur"]:>2}.   {club["change"]}   "
            f"{club["name"]:<20}    {club["games"]:2}    "
            f"{club["win"]:2} {club["draw"]:2} {club["loss"]:2}    "
            f"{club["goals_for"]:3}:{club["goals_against"]:3}    "
            f"{club["goals_difference"]:3}    "
            f"{club["points"]:2}   "
            "│"
            )
    print_line("─", "└", "┘")
    input("Weiter mit <ENTER>...")


print_table(generate_clubs())
