class MainModel:
    def __init__(self):
        self.settings = {"dark_mode": False}

    def toggle_dark_mode(self):
        self.settings["dark_mode"] = not self.settings["dark_mode"]