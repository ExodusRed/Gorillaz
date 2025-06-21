import tkinter as tk

# from model.boot_model import BootModel
from view.base_view import BaseView
# from controller.boot_controller import BootController

class BootView(BaseView):
    def __init__(self, master, scalar: int):
        super().__init__(master)
        # self.boot_model = BootModel() // outsourced to base class
        # self.boot_controller = BootController() // "..."

        self.S = scalar

        self.create_elements()

    def create_elements(self):
        self.texts = self.model.texts

        print(f"font_size: {self.FONT_SIZE * self.S}")
        print(f"scalar: ", self.S)
        print(self.FONT)

        # for i in range(len(self.texts.keys()) - 1):
        #     self.canvas.create_text((self.master.winfo_width() // 2), (i * 30) + 20 * self.S, text=self.texts[list(self.texts.keys())[i]], fill="white", font=(self.FONT, (self.FONT_SIZE * self.S)), anchor="n")
        #     print(self.texts[list(self.texts.keys())[i]])

        # for i in range(len(self.texts.keys()) - 1):
            # self.draw_text()

        self.draw_text(self.canvas, "Hello World!", 100, 100, 1)
        self.draw_text(self.canvas, "HELLO WORLD!", 100, 150, 1)
            


    def show(self):
        self.grid(row=0, column=0, sticky="nsew")

    def hide(self):
        self.grid_remove()

        