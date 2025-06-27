import tkinter as tk
from model.font_model import FontModel
from model.text_model import TextModel

class TextRenderer:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas

    # def draw_text(self, text_model: TextModel, font: FontModel, color: str = "#FFFFFF"):
    #     text_model.clear_from_canvas(self.canvas)

    #     cw, ch = font.get_size()
    #     x0, y0 = text_model.x, text_model.y
    #     text_model.char_rects = []

    #     for idx, ch_ in enumerate(text_model.text):
    #         bitmap = font.get_char_bitmap(ch_)
    #         rects  = []
    #         # x_char = x0 + idx * (cw*text_model.pixel_size + text_model.spacing*text_model.pixel_size)
    #         x_char = x0 + idx * (cw * text_model.pixel_size + text_model.spacing)
    #         # x_char = x0 + idx * (cw + text_model.spacing)
    #         # print(x_char)

    #         for row_i, row in enumerate(bitmap):
    #             for col_i, bit in enumerate(row):
    #                 if bit == "1":
    #                     x1 = x_char + col_i * text_model.pixel_size
    #                     print(f"is 1: {text_model.pixel_size}")
    #                     y1 = y0     + row_i * text_model.pixel_size
    #                     r  = self.canvas.create_rectangle(
    #                            x1, y1,
    #                            x1 + text_model.pixel_size - 1,
    #                            y1 + text_model.pixel_size - 1,
    #                            fill=color, outline=color
    #                         )
    #                     rects.append(r)
    #         text_model.char_rects.append(rects)

    # def draw_text(self, canvas, text, x, y, font, pixel_size=2, spacing=1, color="#FFFFFF"):
    def draw_text(self, canvas, text_model):
    # Draws pixel font text on a canvas.
    
    # - canvas: Tkinter Canvas
    # - text: string to draw
    # - x, y: top-left starting position
    # - font_data: dictionary of characters with 8x8 binary strings
    # - pixel_size: how big each 'pixel' should be
    # - spacing: space between characters
    # - color: color of the 'on' pixels

        for char_index, char in enumerate(text_model.text):
            # char_bitmap = PIXEL_FONT_8X8.get(char)
            # char_bitmap = font.glyphs.get(char)
            # print(font["glyphs"])
            # print(font.glyphs)
            # print(font["glyphs"])
            # char_bitmap = font["glyphs"].get(char)
            # char_bitmap = text_model.font.get_char_bitmap(char)
            # char_bitmap = text_model.FONT.get_char_bitmap(char)
            char_bitmap = text_model.font.get_char_bitmap(char)
            char_size = text_model.font.get_size()
            rects = []

            # print("after rects")
            
            if not char_bitmap:
                # continue  # skip missing characters 
                # char_bitmap = PIXEL_FONT_8X8.get("?") # | or use '?'
                # char_bitmap = font["glyphs"].get("?")
                continue
                # char_bitmap = font.glyphs.get("?")

            char_x = text_model.x + char_index * ((8 * text_model.pixel_size) + text_model.spacing) # font pixel width? Take as arg?
            char_x = text_model.x + char_index * ((5 * text_model.pixel_size) + text_model.spacing)
            char_x = text_model.x + char_index * ((char_size[0] * text_model.pixel_size) + text_model.spacing)

            for row_index, row in enumerate(char_bitmap):
                # print("for row in bitmap")
                for col_index, pixel in enumerate(row):
                    if pixel == '1':
                        r = canvas.create_rectangle(
                            char_x + col_index * text_model.pixel_size,
                            text_model.y + row_index * text_model.pixel_size,
                            char_x + (col_index + 1) * text_model.pixel_size,
                            text_model.y + (row_index + 1) * text_model.pixel_size,
                            outline="",
                            fill=text_model.color
                        )
                        rects.append(r)



       

    # def draw_centered(
    #         self,
    #         text_model: TextModel,
    #         color: str = "#FFFFFF",
    #         area: tuple[int,int,int,int] = None):

    #     if area:
    #         x0, y0, w, h = area
    #     else:
    #         w = self.canvas.winfo_width()
    #         h = self.canvas.winfo_height()
    #         x0 = y0 = 0

    #     text_w, text_h = text_model.get_dimension(self.font)
    #     text_model.x = x0 + (w - text_w) // 2
    #     text_model.y = y0 + (h - text_h) // 2
    #     self.draw_text(text_model, color)