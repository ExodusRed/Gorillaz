import tkinter as tk

from model.char_model import CharModel

from view.base_view import BaseView
from view.char_view import CharView

class PresetView(BaseView):
    def __init__(self, master, scalar):
        super().__init__(master)
        self.S = scalar
        self.current_question_index = 0,
        self.current_input = "",
        # self.input_model
        
        print("Welcome to PresetView!")
        # self.update_idletasks()
        # print(self.S)

        self.QS = {}

        self.center_pos = self.get_center_position()
        

        self.start_asking()


    def start_asking(self):
        # titel_input_model = self.text_model("Hello World!", 100, 100, self.FONT, 1, 1, "#FFFFFF")
        QUESTIONS = self.model.QUESTIONS

        for q_index, _q in enumerate(list(QUESTIONS)):
            # print(f"Q: {QUESTIONS[_q]}")
            # print(f"q_index: {q_index}")
            if q_index == 4:
                # for q in _q
                print("q3 ->")
                # Draw each line of the last question (split by newlines)
                for line_index, line in enumerate(list(QUESTIONS[_q].split("\n"))):
                    q_text = self.text_model(
                        line, 
                        self.center_pos[0] - self.get_text_width(line, self.S, self.S),
                        (line_index * 10 + 20) * self.S,
                        self.FONT,
                        self.S,
                        self.S
                    )
                    self.text_renderer.draw_text(
                        self.canvas,
                        q_text
                    )
            else:
                # Draw the question as a single line
                q_text = self.text_model(
                    QUESTIONS[_q], 
                    self.center_pos[0] - self.get_text_width(QUESTIONS[_q], self.S, self.S),
                    (q_index * 10 + 50) * self.S,
                    self.FONT,
                    self.S,
                    self.S
                )
                self.text_renderer.draw_text(
                    self.canvas,
                    q_text
                )

        # self.text_renderer.draw_centered(titel_input_model)
        # pass

        


    # def update_prompt_and_input(self, char, question_index):
    #     # self.draw_text(
    #     #     self.canvas,
    #     #     text,
    #     #     x = self.center_pos[0] + (self.get_text_width(
    #     #         text,
    #     #         pixel_size = self.S,
    #     #         spacing = self.S,
    #     #         font_width = 5
    #     #     ) // 2),
    #     #     y = 100 * self.S,
    #     #     pixel_size = self.S,
    #     #     spacing = self.S
    #     # )

    #     print("update and prompt")

    #     # font = CharModel(self.FONT["glyphs"][char])
    #     bitmap = self.FONT["glyphs"].get(char, "?")
    #     # font = CharModel(self.FONT["glyphs"].get(char, "?"))
    #     font = CharModel(bitmap)
    #     print(bitmap)



        # self.draw_char_at(self.canvas, font, char, 100, 200, self.S)

