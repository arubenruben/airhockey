from src.Model.composite_drawables.leafs.leafComponent import LeafComponent


class Font(LeafComponent):

    def __init__(self, position, text, color):
        super().__init__(position)
        self._text = text
        self._color = color

    @property
    def text(self):
        return self._text

    @property
    def color(self):
        return self._color
