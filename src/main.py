import tkinter as tk

from controller.game_controller import GameController
from controller.view_controller import ViewController

# import sys
# import os

# Add project root to sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.view_controller = ViewController(self)
        self.game_controller = GameController(self, self.view_controller)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        

        self.start_game()

    def start_game(self):
        self.view_controller.show_view("boot")



if __name__ == "__main__":
    game = Game()
    game.mainloop()