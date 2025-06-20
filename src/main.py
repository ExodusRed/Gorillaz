import tkinter as tk

from controller.game_controller import GameController
from controller.view_controller import ViewController

# from view.boot_view import BootView
# from view.preset_view import PresetView
# from view.intro_view import IntroView
# from view.game_view import GameView

# from model.game_model import GameModel



class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        # Init view Manager here
        # No do it in the controller
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