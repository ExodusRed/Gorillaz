import importlib

# import sys
# import os

# # Add project root to sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


import sys
import os

# Add project root to sys.path
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)


import utils
# utils.add_assets_to_sys_path()
utils.add_root_to_sys_path()


class ViewController:
    def __init__(self, game):
        self.game = game
        self.views = {}
        self.current_view = None

        self.VIRT_W, self.VIRT_H = 320, 200
        
        self.SW, self.SH = self.game.winfo_screenwidth(), game.winfo_screenheight()

        self.S = self.get_scalar()

        # self.S = 1 # Testing

        # self.font = ("Terminal", self.S * 4)

        # if (utils.add_assets_to_sys_path() == 1):
            # from assets.fonts.font import PIXEL_FONT_8X8
            # import assets.font
            # import assets.fonts

            # pass

        self.set_game_size()
        self.center_game()


    def get_scalar(self):
        S = min((self.SW // self.VIRT_W), (self.SH // self.VIRT_H))
        return S

    def set_game_size(self):
        self.game.geometry(f"{self.VIRT_W * self.S}x{self.VIRT_H * self.S}")

    def center_game(self):
        self.game.update_idletasks()
        ww, wh = self.game.winfo_width(), self.game.winfo_height()
        x, y = (self.SW // 2) - (ww // 2), (self.SH // 2) - (wh // 2)
        self.game.geometry(f"+{x}+{y}")


    def show_view(self, name: str):
        if name not in self.views:
            class_name = name.capitalize() + "View"
            module_name = f"view.{name}_view"

            try:
                module = importlib.import_module(module_name)
                view_class = getattr(module, class_name)
                self.views[name] = view_class(self.game, self.S)
            except (ImportError, AttributeError) as e:
                print(f"[ERROR] Could not load view '{name}': {e}")
                return
            
        if self.current_view:
            self.views[self.current_view].hide()

        self.current_view = name
        self.views[self.current_view].show()

    # def draw_char(canvas, char, x, y, pixel_size=4, bg="#000000", fg=None):
    #     bitmap = PIXEL_FONT_8X8.get(char, PIXEL_FONT_8X8.get('?'))

