from .registry import ALL_FONTS

def get_font(name):
    return ALL_FONTS[name]