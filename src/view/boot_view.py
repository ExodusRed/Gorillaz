import tkinter as tk

# from model.boot_model import BootModel
from view.base_view import BaseView
# from controller.boot_controller import BootController

class BootView(BaseView):
    def __init__(self, master, scalar: int):
        super().__init__(master)
        # self.boot_model = BootModel() // outsourced to base class
        # self.boot_controller = BootController() // "..."

        self.S = scalar # not needed, but keep for later adaptability

        # self.focus()
        # self.bind("<Key>", lambda e: print(e.keysym))

        # titel_input_model = self.text_model("Hello World!", 100, 100, self.FONT, 1, 1, "#FFFFFF")

        # self.text_renderer.draw_text(titel_input_model, self.FONT)
        # donkey = self.text_renderer.draw_text(self.canvas, "Donkey", 100, 100, self.FONT, 1, 1)

        txt = self.text_model("Donkey", 100, 100, self.FONT, 1*self.S, self.S*1)
        

        # self.after(2000, txt.clear_from_canvas(self.canvas))
        # txt = TextModel("")

        # self.text_renderer.draw_text(self.canvas, txt)

        # draw_text(canvas, text, x, y, font, pixel_size=2, spacing=1, color="#FFFFFF"):

        # self.after(1000, lambda: donkey.)

        self.elements = {}

        self.create_elements()

    def create_elements(self):
        texts = self.model.texts

        # for i in range(len(self.texts.keys()) - 1):
        #     self.canvas.create_text((self.master.winfo_width() // 2), (i * 30) + 20 * self.S, text=self.texts[list(self.texts.keys())[i]], fill="white", font=(self.FONT, (self.FONT_SIZE * self.S)), anchor="n")
        #     print(self.texts[list(self.texts.keys())[i]])

        # text_cords = [
        #     (),
        #     (),
        #     (),
        #     ()
        #     ]

        x_cords = (50, 80, 100, 280)
        self.center_pos = self.get_center_position()

        self.text_models, text_objects = [], []
        
        for text_index, text in enumerate(texts):
            if text == "mission_objective":
                print("mission_objective")
                for line_index, line in enumerate(list(texts[text].split("\n"))):
                    print(line)

                    temp_text_model = self.text_model(
                        text = line,
                        x = 0,
                        y = 0,
                        font_model = self.FONT,
                        pixel_size = self.S,
                        spacing = self.S
                    )
                        


                    self.text_models.append(
                    self.text_renderer.draw_text(
                        self.canvas,
                        self.text_model(
                            text = line,
                            x = (self.center_pos[0]) - (self.get_text_width(temp_text_model) // 2),
                            y = (x_cords[text_index] * self.S) + (line_index * 10) * self.S,
                            font_model = self.FONT,
                            pixel_size = self.S,
                            spacing = self.S
                        ),
                    )
                )

            else:
                text_model = self.text_model(
                    text = texts[text],
                    x = 0,
                    y = 0,
                    font_model = self.FONT,
                    pixel_size = self.S * 2 if text_index == 0 else self.S,
                    spacing = self.S
                )


                self.text_models.append(
                    self.text_renderer.draw_text(
                        self.canvas,
                        self.text_model(
                            text = texts[text],
                            x = (self.center_pos[0]) - (self.get_text_width(text_model) // 2),
                            y = x_cords[text_index] * self.S,
                            font_model = self.FONT,
                            pixel_size = self.S * 2 if text_index == 0 else self.S,
                            spacing = self.S
                        ),
                    )
                )




        # for text_index, text in enumerate(texts):
        #     self.text_models.append(
        #         self.text_renderer.draw_text(
        #             self.canvas,
        #             self.text_model(
        #                 text = texts[text],
        #                 x = (self.get_center_position()[0]) - (self.get_text_width(
        #                     texts[text], self.S * 2 if text_index == 0 else self.S, 1, 5) // 2),
        #                 y = x_cords[text_index] * self.S,
        #                 font_model = self.FONT,
        #                 pixel_size = self.S * 2 if text_index == 0 else self.S,
        #                 spacing = 1
        #             ),
        #         )
        #     )



        # for text_index, text in enumerate(texts):
        #     self.text_models.append(
        #         self.text_renderer.draw_text(
        #             self.canvas,
        #             self.text_model(
        #                 text = texts[text],
        #                 x = (self.get_center_position()[0]) - (self.get_text_size(
        #                     texts[text], (6 if text_index == 0 else 5), (11 if text_index == 0 else 9), self.S, 1)[0] // 2),
        #                 y = x_cords[text_index],
        #                 font_model = self.FONT,
        #                 pixel_size = self.S if text_index == 0 else 1,
        #                 spacing = 1
        #             ),
        #         )
        #     )


            
