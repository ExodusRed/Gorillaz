# MVC dataflow is controlled here

from controller.view_controller import ViewController

from view.boot_view import BootView
from view.presets_view import PresetsView
from view.intro_view import IntroView
# from view.game_view import GameView

class MainController:
    def __init__(self, root):
        self.player1_name: str = ""
        self.player2_name: str = ""
        self.gravity: float = 9.8

        self.view_controller = ViewController(root, controller=self)
        # self.view_controller = ViewController(root, self)


        self.view_controller.register_view("boot", BootView)
        self.view_controller.register_view("presets", PresetsView)
        self.view_controller.register_view("intro", IntroView)
        # self.view_controller.register_view("")

        # for names in ("boot", "presets", "intro", "game"):
            # self.view_controller.register_view(names)

        self.view_controller.show_view("boot")

    def start_game(self):
        pass

    def on_presets_done(self, player1_name: str, player2_name: str, gravity: float):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.gravity = gravity

        # self.view_controller.show_view("intro", player1=player1_name, player2=player2_name)

    # Call View Controller here