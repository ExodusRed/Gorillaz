import tkinter as tk

from model.char_model import CharModel

from view.base_view import BaseView
from view.char_view import CharView

class PresetView(BaseView):
    def __init__(self, master, scalar):
        super().__init__(master)
        self.S = scalar
        
        print("Welcome to PresetView!")
        # self.update_idletasks()
        # print(self.S)

        self.center_pos = self.get_center_position()
        

        self.start_asking()


    def start_asking(self):
        # titel_input_model = self.text_model("Hello World!", 100, 100, self.FONT, 1, 1, "#FFFFFF")

        # self.text_renderer.draw_centered(titel_input_model)
        pass

        

    # def start_asking(self):
    #     c = 0
    #     text = self.model.TEXT[f"q{c}"]
    #     center_x = self.get_center_position()[0]
    #     print(f"center_x = {self.get_center_position()[0]}")
    #     # center_x = 100
    #     q0 = self.draw_text(
    #         self.canvas, text,
    #         x = center_x - (self.get_text_width(text,
    #             pixel_size = self.S,
    #             spacing = self.S,
    #             font_width = 5
    #         ) // 2) - 50 * self.S,
    #         y = 100 * self.S,
    #         font = self.FONT,
    #         pixel_size = self.S,
    #         spacing = self.S
    #     )
    def update_prompt_and_input(self, char, question_index):
        # self.draw_text(
        #     self.canvas,
        #     text,
        #     x = self.center_pos[0] + (self.get_text_width(
        #         text,
        #         pixel_size = self.S,
        #         spacing = self.S,
        #         font_width = 5
        #     ) // 2),
        #     y = 100 * self.S,
        #     pixel_size = self.S,
        #     spacing = self.S
        # )

        print("update and prompt")

        # font = CharModel(self.FONT["glyphs"][char])
        bitmap = self.FONT["glyphs"].get(char, "?")
        # font = CharModel(self.FONT["glyphs"].get(char, "?"))
        font = CharModel(bitmap)
        print(bitmap)



        # self.draw_char_at(self.canvas, font, char, 100, 200, self.S)

