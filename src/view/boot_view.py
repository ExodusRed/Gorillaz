import tkinter as tk

# from model.boot_model import BootModel
from view.base_view import BaseView
# from controller.boot_controller import BootController

class BootView(BaseView):
    def __init__(self, master, scalar: int):
        super().__init__(master)
        # self.boot_model = BootModel()
        # self.boot_controller = BootController()

        self.S = scalar
        # self.S = 1

        self.create_elements()

    def create_elements(self):
        # copyleft
        self.texts = self.boot_model.texts
            
        # for item in self.boot_model.texts:
            # print(item)
        # self.canvas = tk.self.Canvas()

        # print(self.master.winfo_width(), self.master.winfo_height())

        # self.prompt_frame = tk.Frame(self.canvas, bg="red")
        # self.prompt_frame.grid(row=0, column=0, sticky="nsew")

        print(f"font_size: {self.FONT_SIZE * self.S}")
        print(f"scalar: ", self.S)
        print(self.FONT)

        for i in range(len(self.texts.keys()) - 1):
            self.canvas.create_text((self.master.winfo_width() // 2), (i * 30) + 20 * self.S, text=self.texts[list(self.texts.keys())[i]], fill="white", font=(self.FONT, (self.FONT_SIZE * self.S)), anchor="n")
            print(self.texts[list(self.texts.keys())[i]])


    def show(self):
        self.grid(row=0, column=0, sticky="nsew")

    def hide(self):
        self.grid_remove()

        