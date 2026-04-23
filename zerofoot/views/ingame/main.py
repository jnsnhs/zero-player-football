from ..view import View


class GameMainScreen(View):

    def __init__(self, database) -> None:
        super().__init__()
        self.database = database
        self.print_heading("Sonntag, 1. Juni 1965")
        print(f"\nSie sind Anhänger von {database.user.club.name} und\n"
              "fiebern dem nächsten Spieltag entgegen.\n")
        print("\n[1] Verein ansehen\n")
        print("[2] Tabelle ansehen\n\n")
        print("[0] Hauptmenü")
        user_input = input(self.PROMPT_PREFIX).strip()
        match user_input:
            case "1":
                ClubSummaryScreen(database)
                self.__init__(database)
            case "2":
                DomesticLeagueTableScreen(database)
                self.__init__(database)
            case "0":
                return
            case _:
                self.__init__(database)


class DomesticLeagueTableScreen(View):

    def __init__(self, database) -> None:
        super().__init__()
        self.database = database
        print("Hier wird die Tabelle der Liga zu sehen sein")
        print("Zurück mit <ENTER>...")
        input(self.PROMPT_PREFIX)


class ClubSummaryScreen(View):

    def __init__(self, database) -> None:
        super().__init__()
        self.database = database
        self.print_heading(database.user.club.name)
        print(database.user.club)
        print("Zurück mit <ENTER>...")
        input(self.PROMPT_PREFIX)
