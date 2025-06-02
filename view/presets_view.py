import tkinter as tk

class PresetsView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.name1: str = ""
        self.name2: str = ""
        self.gravity: float = ""

        self.controller = controller

        self.controller.on_presets_done(self.name1, self.name2, self.gravity)

