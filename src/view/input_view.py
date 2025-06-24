from model.char_model import CharModel
from model.font_model import FontModel

class InputView:
    def __init__(self, text, font):
        self.text = text
        self.font = font

    def create_char(self, char: str, font_model: FontModel, )