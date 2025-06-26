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

        # print(f"font_size: {self.FONT_SIZE * self.S}")
        # print(f"scalar: ", self.S)
        # print(self.FONT)

        # for i in range(len(self.texts.keys()) - 1):
        #     self.canvas.create_text((self.master.winfo_width() // 2), (i * 30) + 20 * self.S, text=self.texts[list(self.texts.keys())[i]], fill="white", font=(self.FONT, (self.FONT_SIZE * self.S)), anchor="n")
        #     print(self.texts[list(self.texts.keys())[i]])

        # for i in range(len(self.texts.keys()) - 1):
            # self.draw_text()

        self.update_idletasks()
        self.update()

        # center_x = self.master.winfo_width() // 2
        # center_y = self.master.winfo_height() // 2

        self.center_pos = self.get_center_position()
        print(f"self.center_pos: {self.center_pos}")

        # print(self.center_pos[0], self.center_pos[1])

        txt = "Hello World!\nABC123"
        txt = "The quick brown fox jumps over the lazy dog (yolo)"
        

        txt1 = self.text_model(txt, 100, 100, self.FONT, 1, 1)
        txt2 = self.text_model(txt, 100, 150, self.FONT, self.S, 1)

        txtb = self.text_model(txt, 100, 200, self.FONT_B, self.S, 1)


        # print(self.FONT_B)

        
        txt_box = self.text_renderer.draw_text(self.canvas, txt1)
        txt_box2 = self.text_renderer.draw_text(self.canvas, txt2)

        txt_b = self.text_renderer.draw_text(self.canvas, txtb)

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

        x_pos = 0

        # self.elements["title"] = self.text_model(
            # texts["title"],
            # x = self.center_pos - self.text_model.get_dimension(self.FONT)
            # )

        # self.title = self.draw_text(
        #     self.canvas,
        #     text=texts["title"],
        #     x=(self.center_pos[0]) - (self.get_text_width(texts["title"], self.S, 2) // 2),
        #     y=60 * self.S,
        #     font=self.FONT_B,
        #     pixel_size=self.S,
        #     spacing=2
        # )

        # self.legal_notice = self.draw_text(
        #     self.canvas, text=texts["legal_notice"],
        #     x=(self.center_pos[0]) - self.get_text_width(texts["legal_notice"], self.S) // 2,
        #     y=90 * self.S, pixel_size=self.S
        #     )

        # for line_index, line in enumerate(texts["mission_objective"].split("\n")):
        #     # print(len(line) * (5 + 1)) - this line actually saved me
            
        #     text_width = self.get_text_width(line, pixel_size=self.S, spacing=self.S, font_width=self.FONT["width"])


        #     print(f"text width: {text_width}")


        #     print(((self.VIRT_W * self.S) // 2) - (text_width // 2))

        #     # self.draw_text(self.canvas, line, (self.center_pos[0] // 2) - (text_width // 2), (line_index * 20) + 100, self.S * 1, spacing)
        #     self.draw_text(self.canvas, line, x=(self.center_pos[0]) - (text_width // 2), y=((line_index) * 16 + 120) * self.S, pixel_size=self.S, spacing=self.S)


        # self.draw_text(self.canvas, texts["prompt"], (self.center_pos[0] - (text_width // 2)), 100)

        # self.prompt = self.draw_text(
        #     self.canvas,
        #     text = texts["prompt"],
        #     x = self.center_pos[0] - self.get_text_width(texts["prompt"], self.S, self.S) // 2,
        #     y = 260 * self.S,
        #     pixel_size = self.S,
        #     spacing = self.S
        # )





        

        # txt_width = len(txt) * font_size + spacing

        # self.draw_text(self.canvas, txt, center_x, 100, 1)
        # self.draw_text(self.canvas, "HELLO WORLD!", center_x, 150, 1)
            


    # def show(self):
    #     self.grid(row=0, column=0, sticky="nsew")

    # def hide(self):
    #     self.grid_remove()

        