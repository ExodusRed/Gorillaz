from model.font_model import FontModel

# from tkinter import Canvas as tk
# import tkinter as tk

class TextModel:
    def __init__(self, text: str, x: int, y: int, font: FontModel, pixel_size: int, spacing: int, color="#FFFFFF"):
        self.text = text
        self.x = x
        self.y = y
        self.font = FontModel
        self.pixel_size = pixel_size
        self.spacing = spacing
        self.color = color
        # self.char_rects = list[list[list[int]]] = []
        self.char_rects = []

    def clear_from_canvas(self, canvas):
        for char_rect_list in self.char_rects:
            for rect_id in char_rect_list:
                canvas.delete(rect_id)
        self.char_rects.clear()

    def get_dimension(self, font_model) -> tuple[int, int]:
        char_w, char_h = font_model.get_size()
        print(f"char_w: {char_w}, char_h: {char_h}")
        cell_w = char_w * self.pixel_size
        cell_h = char_h * self.pixel_size

        n = len(self.text)
        if n == 0:
            return (0, cell_h)
        
        total_width = n * cell_w + (n - 1) * self.spacing * self.pixel_size
        total_height = cell_h

        return (total_width, total_height)
