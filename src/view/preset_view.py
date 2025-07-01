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

        # self.caret_position = 
        self.current_input = ""
        self.current_input_text = None
        
        # print("Welcome to PresetView!")

        self.QUESTIONS = self.model.QUESTIONS
        

        self.QS = {}
        # self.AS = {}

        self.questions = []

        self.center_pos = self.get_center_position()


        self.start_asking()

    def ask_next(self):
        self.qc += 1
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
        # self.current_input.
        print(self.model.answers[f"a{self.qc}"])
        self.current_input.clear_from_canvas(self.canvas)

    def update_input(self, char):
        print("view: ", char)
        # append letter at location from current_input + (letter_width + spacing * pxiel_size (self.S))
        # self.current_input

        # self.current_char_location = 

        # self.caret["elem"].clear_from_canvas(self.canvas)

        

        # if char == " ":
        #     self.caret["elem"].clear_from_canvas(self.canvas)
        #     self.current_input_position[0] += (self.FONT.get_size()[0] * self.S + self.S)
        #     self.caret["elem"].x = self.current_input_position[0]

        #     self.model.answers[f"a{self.qc}"] + char

        #     return
            

        # else:

        # if char == " ":

        self.model.answers[f"a{self.qc}"] += char

        if self.current_input != "":
            self.current_input.clear_from_canvas(self.canvas)
    

        self.current_input = self.text_model(
            text = self.model.answers[f"a{self.qc}"],
            x = self.current_input_position[0],
            y = self.current_input_position[1],
            font_model = self.FONT,
            pixel_size = self.S,
            spacing = self.S
        )

        # self.current_input_position[0] += (self.FONT.get_size()[0] * self.S + self.S)

        # self.caret_position[0] += ((self.FONT.get_size()[0] * self.S) + self.S) * len(self.model.answers[f"a{self.qc}"])

        # self.caret["elem"].move(10)

        # self.caret["elem"].clear_from_canvas(self.canvas)

        # self.caret["elem"].x = self.current_input_position[0]
        # self.caret["elem"].y = self.current_input_position[1]

        # self.caret["elem"].y = 

        # todo:
        # draw char
        # update location

        self.model.answers[f"a{self.qc}"] + char

    
        self.caret["elem"].clear_from_canvas(self.canvas)

        self.text_renderer.draw_text(
            self.canvas,
            self.current_input
        )
    
    def start_asking(self):
        print("start asking")
        user_input = []
        if self.qc == 4:
                # for q in _q
            print("q3 ->")
            # Draw each line of the last question (split by newlines)
            for line_index, line in enumerate(list(self.QUESTIONS[list(self.QUESTIONS.keys())[self.qc]].split("\n"))):
                q_text = self.text_model(
                    text = line, 
                    x = (self.center_pos[0]) - (self.get_text_width(line, self.S, self.S, 5) // 2),
                    y = (line_index * 10 + 200) * self.S,
                    font_model = self.FONT,
                    pixel_size = self.S,
                    spacing = self.S
                )
                self.questions.append(q_text)
                 
        else:
            # Draw the question as a single line
            element_width = self.get_text_width(self.QUESTIONS[list(self.QUESTIONS.keys())[self.qc]], self.S, self.S, 5)
            element_x = ((self.center_pos[0]) - (element_width // 2)) - (60 * self.S)
            element_y = (self.qc * 16 + 80) * self.S

            q_text = self.text_model(
                text = self.QUESTIONS[list(self.QUESTIONS.keys())[self.qc]],
                x = element_x,
                y = element_y,
                font_model = self.FONT,
                pixel_size = self.S,
                spacing = self.S
            )

            a_text = self.text_model(
                text = "",
                x = 0,
                y = 0,
                font_model = self.FONT,
                pixel_size = self.S,
                spacing = self.S
            )

            self.text_renderer.draw_text(
                self.canvas,
                q_text
            )

            self.questions.append(q_text)
            self.model.answers[f"a{self.qc}"] = ""
            # self.model.answers[f"a{self.qc}"].text = a_text

            if (self.qc == 0):
                self.input = self.text_model(
                    "",
                    x = 0,
                    y = 0,
                    font_model = self.FONT,
                    pixel_size = self.S,
                    spacing = self.S,
                )

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

            
            # self.current_input_position[0] = element_x + element_width

            # self.current_input_position[0] = element_x + element_width

            self.caret_position[0] = element_x + element_width
            self.caret_position[1] = element_y
            
            # self.current_input_position[1] = element_y

            # self.caret["elem"].x = element_x + element_width + (self.S + self.S)
            # self.caret["elem"].x = self.current_input_position[0] + (self.FONT.get_size()[0] * self.S + self.S)

            self.caret["elem"].x = self.caret_position[0]
            self.caret["elem"].y = self.caret_position[1]

            self.input.x = self.caret_position[0]

            print(f"self.caret_position: ", self.caret_position)

            self.input.x = self.caret_position[0]
            

            self.text_renderer.draw_text(self.canvas, self.caret["elem"])
        













    # def start_asking(self):
    #     # titel_input_model = self.text_model("Hello World!", 100, 100, self.FONT, 1, 1, "#FFFFFF")
    #     QUESTIONS = self.model.QUESTIONS

    #     for q_index, _q in enumerate(list(QUESTIONS)):
    #         # print(f"Q: {QUESTIONS[_q]}")
    #         # print(f"q_index: {q_index}")
    #         if q_index == 4:
    #             # for q in _q
    #             print("q3 ->")
    #             # Draw each line of the last question (split by newlines)
    #             for line_index, line in enumerate(list(QUESTIONS[_q].split("\n"))):
    #                 q_text = self.text_model(
    #                     line, 
    #                     # self.center_pos[0] - self.get_text_width(line, self.S, self.S),
    #                     (self.center_pos[0]) - (self.get_text_width(line, self.S, self.S, 5) // 2),
    #                     (line_index * 10 + 200) * self.S,
    #                     self.FONT,
    #                     self.S,
    #                     self.S
    #                 )
    #                 self.question_text_models[f"q{q_index}"] = self.text_renderer.draw_text(
    #                     self.canvas,
    #                     q_text
    #                 )
    #         else:
    #             # Draw the question as a single line
    #             q_text = self.text_model(

    #                 text = QUESTIONS[_q],
    #                 x = ((self.center_pos[0]) - (self.get_text_width(QUESTIONS[_q], self.S, self.S, 5) // 2)) - (60 * self.S),
    #                 y = (q_index * 16 + 80) * self.S,
    #                 font_model = self.FONT,
    #                 pixel_size = self.S,
    #                 spacing = self.S
    #             )
    #             self.text_renderer.draw_text(
    #                 self.canvas,
    #                 q_text
    #             )











    # def start_asking(self):

    #     if self.qc == 4:
    #             # for q in _q
    #             print("q3 ->")
    #             # Draw each line of the last question (split by newlines)
    #             for line_index, line in enumerate(list(self.QUESTIONS[list(self.QUESTIONS.keys())[self.qc]].split("\n"))):
    #                 q_text = self.text_model(
    #                     line, 
    #                     # self.center_pos[0] - self.get_text_width(line, self.S, self.S),
    #                     (self.center_pos[0]) - (self.get_text_width(line, self.S, self.S, 5) // 2),
    #                     (line_index * 10 + 200) * self.S,
    #                     self.FONT,
    #                     self.S,
    #                     self.S
    #                 )
    #                 self.question_text_models[f"q{self.qc}"] = self.text_renderer.draw_text(
    #                     self.canvas,
    #                     q_text
    #                 )















                # self.text_models.append(
                # self.text_renderer.draw_text(
                #     self.canvas,
                #     self.text_model(
                #         text = line,
                #         x = (self.center_pos[0]) - (self.get_text_width(
                #             line, self.S, self.S, 5) // 2),
                #         y = (100 * self.S) + (line_index * 10) * self.S,
                #         font_model = self.FONT,
                #         pixel_size = self.S,
                #         spacing = self.S
                #     ),
                # )





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

