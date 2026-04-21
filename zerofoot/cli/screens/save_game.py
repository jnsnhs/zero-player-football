from ...cli.screens.screen import Screen


class NewGameScreen(Screen):

    def __init__(self) -> None:
        super().__init__()
        print("Speichere dein Spiel...")
        input("> ")
