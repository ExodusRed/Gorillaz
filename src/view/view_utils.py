# from assets.fonts.font import PIXEL_FONT_8X8
# from assets.fonts.font8x8 import PIXEL_FONT_5X7 as PIXEL_FONT_8X8
# from assets.fonts.font5x9 import PIXEL_FONT_5X9 as PIXEL_FONT_8X8

from assets.fonts.registry import ALL_FONTS

from model.font_model import FontModel
from model.text_model import TextModel

from model.char_model import CharModel
from view.char_view import CharView

from view.renderer.text_renderer import TextRenderer

def get_font(name):
    return ALL_FONTS[name]

# def draw_text(canvas, text, x, y, font=get_font("5x9"), pixel_size=2, spacing=1, color="#FFFFFF"):
#     # Draws pixel font text on a canvas.
    
#     # - canvas: Tkinter Canvas
#     # - text: string to draw
#     # - x, y: top-left starting position
#     # - font_data: dictionary of characters with 8x8 binary strings
#     # - pixel_size: how big each 'pixel' should be
#     # - spacing: space between characters
#     # - color: color of the 'on' pixels

#     for char_index, char in enumerate(text):
#         # char_bitmap = PIXEL_FONT_8X8.get(char)
#         # char_bitmap = font.glyphs.get(char)
#         # print(font["glyphs"])
#         # print(font.glyphs)
#         # print(font["glyphs"])
#         char_bitmap = font["glyphs"].get(char)
        
#         if not char_bitmap:
#             # continue  # skip missing characters 
#             # char_bitmap = PIXEL_FONT_8X8.get("?") # | or use '?'
#             char_bitmap = font["glyphs"].get("?")
#             # char_bitmap = font.glyphs.get("?")

#         char_x = x + char_index * ((8 * pixel_size) + spacing) # font pixel width? Take as arg?
#         char_x = x + char_index * ((5 * pixel_size) + spacing)
#         char_x = x + char_index * ((font["width"] * pixel_size) + spacing)

#         for row_index, row in enumerate(char_bitmap):
#             for col_index, pixel in enumerate(row):
#                 if pixel == '1':
#                     canvas.create_rectangle(
#                         char_x + col_index * pixel_size,
#                         y + row_index * pixel_size,
#                         char_x + (col_index + 1) * pixel_size,
#                         y + (row_index + 1) * pixel_size,
#                         outline="",
#                         fill=color
#                     )

# def draw_char_at(canvas, font, char: str, grid_x: int, grid_y: int, pixel_size: list[int], color = "#FFFFFF"):
#     # bitmap = ALL_FONTS[font]["glyphs"].get(char, get_font["?"])
#     bitmap = font["glyphs"].get(char, font["glyphs"]["?"])
#     print(char, bitmap)

#     char_model = CharModel(bitmap)

#     x = grid_x * pixel_size
#     y = grid_y * pixel_size

#     CharView(canvas, char_model, x, y, pixel_size, color)


# def draw_char_at(canvas, char_model , grid_x: int, grid_y: int, pixel_size: list[int], color = "#FFFFFF"):
# def draw_char_at(canvas, char_model , font_width: int, font_height: int, pixel_size: list[int], color = "#FFFFFF"):
#     # bitmap = ALL_FONTS[font]["glyphs"].get(char, get_font["?"])
#     # bitmap = font["glyphs"].get(char, font["glyphs"]["?"])
#     # print(char, bitmap)

#     # char_model = CharModel(bitmap)

#     # x = grid_x * pixel_size
#     x = font_width * pixel_size
#     # y = grid_y * pixel_size
#     y = font_height * pixel_size
    
#     CharView(canvas, char_model, x, y, pixel_size, color)

# def draw_char_at(canvas, char, x, y, font=get_font("5x9"), pixel_size=2, spacing=1, color="#FFFFFF"):
#         char_bitmap = font["glyphs"].get(char)
        
#         if not char_bitmap:
#             # continue  # skip missing characters 
#             # char_bitmap = PIXEL_FONT_8X8.get("?") # | or use '?'
#             char_bitmap = font["glyphs"].get("?")
#             # char_bitmap = font.glyphs.get("?")

#         # char_x = x + char_index * ((8 * pixel_size) + spacing) # font pixel width? Take as arg?
#         char_x = x + char_index * ((5 * pixel_size) + spacing)
#         char_x = x + char_index * ((font["width"] * pixel_size) + spacing)

#         for row_index, row in enumerate(char_bitmap):
#             for col_index, pixel in enumerate(row):
#                 if pixel == '1':
#                     canvas.create_rectangle(
#                         char_x + col_index * pixel_size,
#                         y + row_index * pixel_size,
#                         char_x + (col_index + 1) * pixel_size,
#                         y + (row_index + 1) * pixel_size,
#                         outline="",
#                         fill=color
#                     )


# def draw_text(canvas, text_model: TextModel, font_model: FontModel, spacing: int, color="#FFFFFF"):
#     text_model.char_rects.clear()

#     font_width, font_height = font_model.get_size()
#     x = text_model.x

#     for char in text_model.text:
#         bitmap = font_model.get_char_bitmap(char)
#         char_rects = []

#         for row_index, row in enumerate(bitmap):
#             for col_index, pixel in enumerate(row):
#                 if pixel == '1':
#                     rect = canvas.create_rectangle(
#                         x + col_index * text_model.pixel_size,
#                         text_model.y + row_index * text_model.pixel_size,
#                         x + (col_index + spacing) * text_model.pixel_size,
#                         text_model.y + (row_index + spacing) * text_model.pixel_size,
#                         outline = "",
#                         color = color
#                     )
#                     char_rects.append(rect)
            
#         text_model.char_rects.append(char_rects)
#         x += font_width * text_model.pixel_size + spacing

# def draw_text(canvas, text_model: TextModel, font_model: FontModel, spacing: int, color="#FFFFFF"):
    # pass

# def draw_text(self, canvas, text_model):
    # TextRenderer.draw_text()