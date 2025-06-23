# class CharModel:
#     def __init__(self, canvas, char): # letter will a 2D Array of rectangles ( 5x7 matrix )
#         self.canvas = canvas
#         self.char = char



class CharModel:
    def __init__(self, bitmap: list[str]): # letter will a 2D Array of rectangles ( 5x7 matrix )
        self.bitmap = bitmap

    def get_pixel(self, row: int, column: int):
        return self.bitmap[row][column] == 1