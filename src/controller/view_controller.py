import importlib

import sys
import os


import utils
utils.add_root_to_sys_path()


class ViewController:
    def __init__(self, game):
        self.game = game
        self.views = {}
        self.current_view = None

        # self.VIRT_W, self.VIRT_H = 320, 200
        self.VIRT_W, self.VIRT_H = 640, 350
        
        self.SW, self.SH = self.game.winfo_screenwidth(), game.winfo_screenheight()

        self.S = self.get_scalar()

        self.S = 1 # Testing

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
        print(f"get_scalar(): {S}")
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
