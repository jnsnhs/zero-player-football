from os import path


PROMPT_PREFIX = "\n\n> "
SCREEN_WIDTH = 80
PROJECT_DIR = path.dirname(path.abspath(__file__))
STATIC_DIR = path.join(PROJECT_DIR, "static")
SCENARIOS_DIR = path.join(PROJECT_DIR, "static", "scenarios")
ENCODING = "utf8"
REFEREE_TO_CLUB_RATIO = 0.6


PATH_CLUB_DATA = "./static/club_data_1963.csv"
PATH_TO_LAST_NAMES = "./static/"

AVG_REFEREE_AGE = 38
AVG_GOALS_PER_GAME = 3.5
