from datetime import date
from enum import Enum
from os import path
from random import randint, triangular, choice
from sys import exit
from uuid import uuid4

from ..defaults import STATIC_DIR


class Nationality(Enum):
    """
    According to ISO 3166 Country Codes\n
    https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
    """
    AT = "Österreich"
    DE = "Deutschland"
    NL = "Niederlande"
    RS = "Serbien"
    TR = "Türkei"


class Trait(Enum):
    """
    According to the Big Five Personality Trait Model\n
    https://en.wikipedia.org/wiki/Big_Five_personality_traits
    """
    OP = "Openness"
    CO = "Conscientiousness"
    EX = "Extraversion"
    AG = "Agreeableness"
    NE = "Neuroticism"


class Person:

    def __init__(
        self,
        birthyear: int,
        nationality: Nationality,
    ) -> None:
        self.id = uuid4()
        self.birthdate: str = self.set_birthdate(birthyear)
        self.nationality: Nationality = nationality
        self.first_name: str = self.set_first_name(
            nationality, birthyear)
        self.last_name: str = self.set_last_name(nationality)
        self.full_name: str = f"{self.first_name} {self.last_name}"
        self.personality: dict = self.set_personality()

    def set_personality(self) -> dict:
        personality = {}
        for trait in Trait:
            personality[trait] = int(triangular(0, 1, 0.5) * 5 + 1)
        return personality

    def set_birthdate(self, year: int) -> str:
        month = randint(1, 12)
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = randint(1, 31)
        elif month in [4, 6, 9, 11]:
            day = randint(1, 30)
        else:
            day = randint(1, 28)
        random_birthdate = f"{year}-{month}-{day}"
        return random_birthdate

    def set_first_name(self, nationality: Nationality, birthyear: int) -> str:
        decade = birthyear // 10 * 10
        try:
            file_name = f"first_names_{nationality.name}_m_{decade}.txt"
            path_to_file = path.join(STATIC_DIR, "first_names", file_name)
            with open(path_to_file, "r", encoding="utf8") as file:
                first_names = file.readlines()
        except FileNotFoundError:
            try:
                file_name = f"first_names_{nationality.name}_m.txt"
                path_to_file = path.join(STATIC_DIR, "first_names", file_name)
                with open(path_to_file, "r", encoding="utf8") as file:
                    first_names = file.readlines()
            except Exception:
                print(f"Die Datei {file_name} konnte nicht gelesen werden. "
                      "Das Programm wird beendet.")
                exit(0)
        random_first_name = choice(first_names).strip("\n")
        return random_first_name

    def set_last_name(self, nationality: Nationality) -> str:
        file_name = f"last_names_{nationality.name}.txt"
        path_of_file = path.join(STATIC_DIR, "last_names", file_name)
        try:
            with open(path_of_file, "r", encoding="utf8") as file:
                last_names = file.readlines()
        except Exception:
            print(f"Die Datei {file_name} konnte nicht gelesen werden. "
                  "Das Programm wird beendet.")
            exit(0)
        random_last_name = choice(last_names).strip("\n")
        return random_last_name

    def get_age(self, today: date) -> int:
        birthday = date.fromisoformat(self.birthdate)
        age = today.year - birthday.year
        if (today.month < birthday.month or
                today.month == birthday.month and today.day < birthday.day):
            age -= 1
        return age

    def __str__(self) -> str:
        lines = f"{self.full_name}, *{self.birthdate.split("-")[0]}"
        return lines
