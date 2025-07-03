import tkinter as tk
import importlib


# from model.char_model import CharModel
# from model.font_model import FontModel

from model.font_model import FontModel
from model.text_model import TextModel

# import view.view_utils as view_utils
# from view.view_utils import draw_text, get_font
from view.view_utils import get_font
from view.renderer.text_renderer import TextRenderer


class BaseView(tk.Frame):
    FG = "#FFFFFF"
    BG = "#000000"
    # FONT = "Terminal"
    # FONT = "Fixedsys"
    # FONT = "System"

    # FONT = get_font("5x9")
    # FONT_B = get_font("5x9b")

    # FONT = FontModel()

    # FONT_SIZE = 6

    def __init__(self, master, scalar=None, *args, **kwargs):
        super().__init__(master, bg=self.BG, *args, **kwargs)
        # self.controller = controller
        # self.model = model


        self.master = master

        self.canvas = tk.Canvas(self, bg=self.BG)
        self.canvas.pack(fill="both", expand=True)

        
        self.text_renderer = TextRenderer(self.canvas)

        base_name = self.__class__.__name__.replace("View", "").lower()
        class_prefix = base_name.capitalize()

        # self.FONT = get_font("5x9")
        #
        # self.FONT_B = get_font("5x9b")

        self.FONT = FontModel("5x9", get_font("5x9")["glyphs"])
        self.FONT_B = FontModel("6x9b", get_font("6x11b")["glyphs"])

        # self.font_model = FontModel()

        self.text_model = TextModel




        # Dynamically import model
        try:
            model_module = importlib.import_module(f"model.{base_name}_model")
            model_class = getattr(model_module, f"{class_prefix}Model")
            self.model = model_class()
            print(self.model)
            print(model_class)
        except (ImportError, AttributeError) as e:
            print(f"[BaseView] Warning: Failed to load Model for {base_name} → {e}")
            self.model = None

        # Dynamically import controller
        try:
            controller_module = importlib.import_module(f"controller.{base_name}_controller")
            controller_class = getattr(controller_module, f"{class_prefix}Controller")
            self.controller = controller_class(self, self.model)
        except (ImportError, AttributeError) as e:
            print(f"[BaseView] Warning: Failed to load controller for {base_name} → {e}")
            self.controller = None


        self.S = scalar
        self.VIRT_W = self.master.view_controller.VIRT_W
        self.VIRT_H = self.master.view_controller.VIRT_H

        # self.CENTER_POS = self.get_center_position() # Or is it not a static var?


        # self.canvas = tk.Canvas(self, bg=self.BG)
        # self.canvas.pack(fill="both", expand=True)

    # def get_font(self, size=None):
    #     return (self.FONT, size if size else self.FONT_SIZE)
    
    def style_kwargs(self, override=None):
        style = {
            "fg": self.FG,
            "bg":self.BG,
            "font": self.get_font()
        }
        if override:
            style.update(override)
        return style
    


    def get_text_size(self, text: str, font_width: int, font_height: int, scalar: int, spacing: int):
        return (
            # (len(text) * font_width) * scalar + len(text) * spacing,
            # font_height * scalar

            (len(text) * font_width) + len(text) * spacing,
            font_height
        )


    def get_center_position(self):
        self.update_idletasks()
        print(self.VIRT_W, self.S)
        # return ((self.VIRT_W * self.S) // 2, (self.VIRT_H * 8) // 2)
        print(f"VIRT_W: {self.VIRT_W}, VIR_H: {self.VIRT_H}, SCALAR: {self.S}")
        return ((self.VIRT_W * self.S) // 2, (self.VIRT_H * self.S) // 2)


    def get_text_width(self, text_object):
        return ((text_object.pixel_size * text_object.font.get_size()[0]) + text_object.spacing) * len(text_object.text)
    
    # def get_text_width(self, text, pixel_size = 1, spacing = 1, font_width = 5):
        # print(f"font_width: {(pixel_size * font_width) + spacing}")
        # print(f"text_width: {((pixel_size * font_width) + spacing) * len(text)}")
        # return ((pixel_size * font_width) + spacing) * len(text)
    

    
    def show(self):
        self.grid(row=0, column=0, sticky="nsew")

    def hide(self):
        self.grid_remove()