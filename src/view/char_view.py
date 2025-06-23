from model.char_model import CharModel

class CharView:
    def __init__(self, canvas, model: CharModel, x: int, y: int, pixel_size: int, color="#FFFFFF"):
        self.canvas = canvas
        self.model = model
        self.x = x
        self.y = y
        self.ps = pixel_size
        self.color = color

        self.rows = len(self.model.bitmap)
        self.columns = len(self.model.bitmap[0])

        self.rect_ids = [[None]*self.columns for _ in range(self.rows)]
        self._draw()


    def _draw(self):
        for row in range(len(self.model.bitmap)):
            for column in range(len(self.model.bitmap[row])):
                if self.model.get_pixel(row, column):
                    x1 = self.x + column * self.ps
                    y1 = self.y + row * self.ps
                    x2 = x1 + self.ps
                    y2 = y2 + self.ps
                    rect = self.canvas.create_rectangle(
                        x1, y1, x2, y2,
                        fill = self.color, outline=self.color
                    )

    def clear(self):
        self.canvas.delete(self.tag)
                    