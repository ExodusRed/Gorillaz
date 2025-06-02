# class Style():
#     def __init__(self, **kwargs):
#         for key, val in kwargs.items():
#             self.key = kwargs.get("bg", )
#             print(key, val)


class Style():
    def __init__(self, bg, fg, font, font_size):
        self.bg = bg
        self.fg = fg
        self.font = font
        self.font_size = font_size
        self.title_font_size = int(font_size*1.2)

        

        self.title_font_size = 18

        # print(self.font_size, self.title_font_size)
