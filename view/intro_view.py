import tkinter as tk

class IntroView(tk.Frame):
    def __init__(self, master, controller, player1="", player2=""):
        super().__init__(master)
        self.controller = controller
        self.label = tk.Label(self, text="")
        self.label.pack()

        self.label.config(text=f"Starring {player1} and {player2}")

    def on_show(self, player1="", player2=""):
        self.label.config(text=f"Starring {player1} and {player2}")
        self.after(3000, self.controller.start_game)
        

