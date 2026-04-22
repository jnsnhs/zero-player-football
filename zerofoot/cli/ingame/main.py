from ...cli.screens.screen import Screen


class GameMainScreen(Screen):

    def __init__(self, database) -> None:
        super().__init__()
        self.database = database
        print("INGAME MAIN SCREEN\n")
        print("[1] Verein ansehen")
        print("[2] Tabelle ansehen\n")
        print("[0] Hauptmenü")
        user_input = input("\n> ").strip()
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


class DomesticLeagueTableScreen(Screen):

    def __init__(self, database) -> None:
        super().__init__()
        self.database = database
        print("Hier wird die Tabelle der Liga zu sehen sein")
        input("Zurück mit <ENTER>...")


class ClubSummaryScreen(Screen):

    def __init__(self, database) -> None:
        super().__init__()
        self.database = database
        print(database.user.club)
        input("Zurück mit <ENTER>...")
