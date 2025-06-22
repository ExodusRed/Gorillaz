from . import font5x9, font5x9b
# from . import font5x9

ALL_FONTS = {}

def register_font(font):
    name = font["name"]
    ALL_FONTS[name] = font

register_font(font5x9.FONT)
register_font(font5x9b.FONT)