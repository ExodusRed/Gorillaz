import tkinter as tk

from model.char_model import CharModel

from view.base_view import BaseView
from view.char_view import CharView

class PresetView(BaseView):
    def __init__(self, master, scalar):
        super().__init__(master)
        self.S = scalar
        self.current_question_index, self.qc = 0, 0,
        self.current_input_position = [0, 0]
        self.caret_position = [0, 0]


        self.current_input = None
        self.current_input_value = ""


        self.QUESTIONS = self.model.QUESTIONS
        

        self.questions = []
        self.answers = []

        self.center_pos = self.get_center_position()


        self.start_asking()

    def ask_next(self):
        # self.qc += 1
        print(self.model.QUESTIONS)

    def anim_caret(self):
    
        if self.caret["visible"]:
            self.caret["elem"].color = "#000000"
            self.caret["visible"] = False
        else:
            self.caret["elem"].color = "#FFFFFF"
            self.caret["visible"] = True

        self.text_renderer.draw_text(self.canvas, self.caret["elem"])

        if self.caret["running"]:
            self.after(333, self.anim_caret)

    def stop_caret_anim(self):
        self.caret["running"] = False

    def delete_from_input(self):

        print(f"Return: {self.qc}, {self.answers[self.qc].text}")

        # self.current_input_value = self.current_input_value[:-1]

        # self.answers[self.qc].text = self.current_input_value
        self.answers[self.qc].text = self.answers[self.qc].text[:-1]

        self.answers[self.qc].clear_from_canvas(self.canvas)
        self.caret["elem"].clear_from_canvas(self.canvas)

        self.text_renderer.draw_text(self.canvas, self.answers[self.qc])
        # self.current_input.clear_from_canvas(self.canvas)

        # move caret pos to new length of elem
        self.caret["elem"].x = self.get_text_width(self.answers[self.qc])

        self.questions[self.qc]


    def update_input(self, char):
        print("view: ", char)

        self.answers[self.qc].text += char

        self.answers[self.qc].clear_from_canvas(self.canvas)

        self.answers[self.qc].x = self.center_pos[0] + self.questions[self.qc].get_dimension(self.FONT)[0] // 2

        # self.caret["elem"].x = self.answers[self.qc].x

        self.caret["elem"].x = self.answers[self.qc].x + self.answers[self.qc].get_dimension(self.FONT)[0]

        self.caret["elem"].clear_from_canvas(self.canvas)

        # self.caret["running"] = False

        # get new text width here
        



        self.text_renderer.draw_text(
            self.canvas,
            # self.current_input
            self.answers[self.qc]
        )

        self.caret["elem"].clear_from_canvas(self.canvas)
        self.text_renderer.draw_text(self.canvas, self.caret["elem"])

        print(self.current_input_value)
    
    def ask_next(self):
        self.current_input_value = ""

    
        if type(self.model.QUESTIONS[f"q{self.qc}"]) == list:
            for line_index, line in enumerate(list(self.QUESTIONS[list(self.QUESTIONS.keys())[self.qc]].split("\n"))):
                q_text = self.text_model(
                    text = line, 
                    x = (self.center_pos[0]) - (self.get_text_width(line, self.S, self.S, 5) // 2),
                    y = (line_index * 10 + 200) * self.S,
                    font_model = self.FONT,
                    pixel_size = self.S,
                    spacing = self.S
                )

                # move input to current line

                self.questions.append(q_text)
                 
        else:
            question_elem = self.text_model(
                text = self.QUESTIONS[f"q{self.qc}"],
                x = 0,
                y = 0,
                font_model = self.FONT,
                pixel_size = self.S,
                spacing = self.S
            )

            answer_elem = self.text_model(
                text = "",
                x = 0,
                y = 0,
                font_model = self.FONT,
                pixel_size = self.S,
                spacing = self.S
            )

            # element_width = self.get_text_width(self.QUESTIONS[list(self.QUESTIONS.keys())[self.qc]], self.S, self.S, 5)
            element_width = question_elem.get_dimension(self.FONT)[0]

            element_x = (self.center_pos[0] - (element_width // 2))
            element_y = (self.qc * 16 + 80) * self.S

            question_elem.x = element_x
            question_elem.y = element_y

            answer_elem.y = question_elem.y

            # self.caret_position = [element_x + element_width, element_y]
            self.caret_position = [element_x + element_width, element_y]
            self.current_input_position = self.caret_position
      


            self.questions.append(question_elem)
            self.answers.append(answer_elem)

                        

            self.caret_position[1] = element_y

            self.caret["elem"].x = self.caret_position[0]
            self.caret["elem"].y = element_y
 
            print(f"self.caret_position: ", self.caret_position)

            print("appended!")

            print(self.qc)

            self.text_renderer.draw_text(
                self.canvas,
                self.questions[self.qc]
            )



     
            self.text_renderer.draw_text(self.canvas, self.caret["elem"])




    def start_asking(self):


        self.caret = {
            "elem" : self.text_model(
                "_", 100, 100,
                font_model = self.FONT,
                pixel_size = self.S,
                spacing = self.S,
            ),
            "running": True,
            "visible" : True,
        }

        self.anim_caret()
        self.ask_next()

