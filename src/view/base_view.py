import tkinter as tk
import importlib

class BaseView(tk.Frame):
    FG = "#FFFFFF"
    BG = "#000000"
    FONT = "Terminal"
    FONT_SIZE = 6

    def __init__(self, master, scalar=None, *args, **kwargs):
        super().__init__(master, bg=self.BG, *args, **kwargs)
        # self.controller = controller
        # self.model = model
        base_name = self.__class__.__name__.replace("View", "").lower()
        class_prefix = base_name.capitalize()


        # Dynamically import controller
        try:
            controller_module = importlib.import_module(f"controller.{base_name}_controller")
            controller_class = getattr(controller_module, f"{class_prefix}Controller")
            self.controller = controller_class()
        except (ImportError, AttributeError) as e:
            print(f"[BaseView] Warning: Failed to load controller for {base_name} → {e}")
            self.controller = None

        # Dynamically import model
        try:
            model_module = importlib.import_module(f"model.{base_name}_model")
            model_class = getattr(model_module, f"{class_prefix}Model")
            self.model = model_class()
        except (ImportError, AttributeError) as e:
            print(f"[BaseView] Warning: Failed to load Model for {base_name} → {e}")
            self.model = None


        self.scalar = scalar

        self.canvas = tk.Canvas(self, bg=self.BG)
        self.canvas.pack(fill="both", expand=True)

    def get_font(self, size=None):
        return (self.FONT, size if size else self.FONT_SIZE)
    
    def style_kwargs(self, override=None):
        style = {
            "fg": self.FG,
            "bg":self.BG,
            "font": self.get_font()
            }
        if override:
            style.update(override)
        return style