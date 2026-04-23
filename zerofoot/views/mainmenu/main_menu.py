import sys

from ..view import View
from .load_game import LoadGameScreen
from .save_game import SaveGameScreen
from .new_game import NewGameScreen
from ..ingame.main import GameMainScreen


class MainMenuScreen(View):

    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        self.game_running: bool = True if app.database else False
        self.print_heading("Hauptmenü")
        if self.game_running:
            self.pause_menu(self.app)
        else:
            self.start_menu(self.app)

    def start_menu(self, app):
        print(
            "\n[1]  Neues Spiel starten\n\n"
            "[2]  Altes Spiel fortsetzen\n\n"
            "[3]  Programm beenden\n"
            )
        user_input = input(self.PROMPT_PREFIX)
        match user_input:
            case "1":
                self.new_game()
            case "2":
                self.load_game()
            case "3":
                self.quit_game()
            case _:
                pass
        self.__init__(app)

    def pause_menu(self, app):
        print(
            "\n[1]  Laufendes Spiel fortsetzen\n\n\n"
            "[2]  Spielstand speichern\n\n"
            "[3]  Spielstand laden\n\n"
            "[4]  Neues Spiel starten\n\n\n"
            "[5]  Programm beenden\n"
            )
        user_input = input(self.PROMPT_PREFIX)
        match user_input:
            case "1":
                GameMainScreen(self.app.database)
            case "2":
                SaveGameScreen(app.database)
            case "3":
                self.load_game()
            case "4":
                self.new_game()
            case "5":
                self.quit_game()
            case _:
                pass
        self.__init__(app)

    def quit_game(self) -> None:
        self.clear_screen()
        self.print_heading("Hauptmenü")
        if self.game_running:
            print("\nMöchten Sie wirklich das laufende Spiel beenden? (j/n)")
            user_input = input(self.PROMPT_PREFIX)
            if user_input in ["n"]:
                self.__init__(self.app)
            elif user_input not in ["j"]:
                self.quit_game()
        self.clear_screen()
        print("\nProgramm beendet. Auf Wiedersehen!\n")
        sys.exit(0)

    def new_game(self) -> None:
        self.clear_screen()
        self.print_heading("Hauptmenü")
        if self.game_running:
            print("\nMöchten Sie wirklich ein neues Spiel starten? (j/n)")
            user_input = input(self.PROMPT_PREFIX)
            if user_input in ["n"]:
                self.__init__(self.app)
            elif user_input not in ["j"]:
                self.new_game()
        NewGameScreen(self.app)

    def load_game(self) -> None:
        self.clear_screen()
        self.print_heading("Hauptmenü")
        if self.game_running:
            print("\nMöchten Sie wirklich einen Spielstand laden? (j/n)")
            user_input = input(self.PROMPT_PREFIX)
            if user_input in ["n"]:
                self.__init__(self.app)
            elif user_input not in ["j"]:
                self.load_game()
        LoadGameScreen(self.app)
