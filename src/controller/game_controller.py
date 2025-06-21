from controller.view_controller import ViewController
# from model.game_model import GameModel

class GameController:
    def __init__(self, game, view_controller):
        self.game = game
        self.view_controller = view_controller
        # self.game_model = GameModel() # not needed
        self.game.bind("<Escape>", lambda e: self.game.quit())

