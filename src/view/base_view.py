import tkinter as tk

class BaseView(tk.Frame):
    FG = "#fff"
    BG = "#000"
    FONT = "Terminal"
    FONT_SIZE = 6

    def __init__(self, master, scalar=None, *args, **kwargs):
        super().__init__(master, bg=self.BG, *args, **kwargs)
        # self.controller = controller
        # self.model = model
        self.scalar = scalar

        self.canvas = tk.Canvas(self, bg=self.bg)
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