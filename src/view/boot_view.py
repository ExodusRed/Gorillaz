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
        texts = self.model.texts

        # print(f"font_size: {self.FONT_SIZE * self.S}")
        # print(f"scalar: ", self.S)
        # print(self.FONT)

        # for i in range(len(self.texts.keys()) - 1):
        #     self.canvas.create_text((self.master.winfo_width() // 2), (i * 30) + 20 * self.S, text=self.texts[list(self.texts.keys())[i]], fill="white", font=(self.FONT, (self.FONT_SIZE * self.S)), anchor="n")
        #     print(self.texts[list(self.texts.keys())[i]])

        # for i in range(len(self.texts.keys()) - 1):
            # self.draw_text()

        self.update_idletasks()

        center_x = self.master.winfo_width() // 2
        center_y = self.master.winfo_height() // 2

        print(center_x, center_y)

        txt = "Hello World!\nABC123"

        # for text in texts:
        #     text_y = 30
        #     for line_index, line in enumerate(texts[text].split("\n")):
        #         print(line)
        #         self.draw_text(self.canvas, line, 50, (text_y * line_index) + 30, 2)

        
        # for i in range(len(texts) - 2):
        #     text_y = 30
        #     for line_index, line in enumerate(texts[list(texts.keys())[i+1]].split("\n")):
        #         print(line)
        #         self.draw_text(self.canvas, line, 50, (text_y * line_index) + 30, 2)

        for line_index, line in enumerate(texts["mission_objective"].split("\n")):
            print(len(line) * (5 + 1))
            self.draw_text(self.canvas, line, 10, (line_index * 20) + 30, self.S * 1, 0)
        

        # txt_width = len(txt) * font_size + spacing

        # self.draw_text(self.canvas, txt, center_x, 100, 1)
        # self.draw_text(self.canvas, "HELLO WORLD!", center_x, 150, 1)
            


    def show(self):
        self.grid(row=0, column=0, sticky="nsew")

    def hide(self):
        self.grid_remove()

        