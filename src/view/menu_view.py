import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, master, controller):
        super().__init__()
        self.create_widgets()
        # self["bg"] = "black"
        # self.style = style
        self.master = master
        self.controller = controller

    def create_widgets(self):
        main_label = tk.Label(self, text="Menu", bg="black")
        main_label.grid()