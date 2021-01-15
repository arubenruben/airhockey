from src.Model.drawables.drawable import Drawable


class Font(Drawable):

    def __init__(self, position, color, text):
        super().__init__(position)
        self._color = color
        self._text = text

    @property
    def text(self):
        return self._text

    @property
    def color(self):
        return self._color
