# from assets.fonts.font import PIXEL_FONT_8X8
# from assets.fonts.font8x8 import PIXEL_FONT_5X7 as PIXEL_FONT_8X8
# from assets.fonts.font5x9 import PIXEL_FONT_5X9 as PIXEL_FONT_8X8

from assets.fonts.registry import ALL_FONTS

def get_font(name):
    return ALL_FONTS[name]

def draw_text(canvas, text, x, y, font=get_font("5x9"), pixel_size=2, spacing=1, color="#FFFFFF"):
    # Draws pixel font text on a canvas.
    
    # - canvas: Tkinter Canvas
    # - text: string to draw
    # - x, y: top-left starting position
    # - font_data: dictionary of characters with 8x8 binary strings
    # - pixel_size: how big each 'pixel' should be
    # - spacing: space between characters
    # - color: color of the 'on' pixels

    for char_index, char in enumerate(text):
        # char_bitmap = PIXEL_FONT_8X8.get(char)
        # char_bitmap = font.glyphs.get(char)
        # print(font["glyphs"])
        # print(font.glyphs)
        # print(font["glyphs"])
        char_bitmap = font["glyphs"].get(char)
        
        if not char_bitmap:
            # continue  # skip missing characters 
            # char_bitmap = PIXEL_FONT_8X8.get("?") # | or use '?'
            char_bitmap = font["glyphs"].get("?")
            # char_bitmap = font.glyphs.get("?")

        char_x = x + char_index * ((8 * pixel_size) + spacing) # font pixel width? Take as arg?
        char_x = x + char_index * ((5 * pixel_size) + spacing)
        char_x = x + char_index * ((font["width"] * pixel_size) + spacing)

        for row_index, row in enumerate(char_bitmap):
            for col_index, pixel in enumerate(row):
                if pixel == '1':
                    canvas.create_rectangle(
                        char_x + col_index * pixel_size,
                        y + row_index * pixel_size,
                        char_x + (col_index + 1) * pixel_size,
                        y + (row_index + 1) * pixel_size,
                        outline="",
                        fill=color
                    )

