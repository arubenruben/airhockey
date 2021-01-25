from src.Model.composite_drawables.leafs.leafComponent import LeafComponent


class Rectangle(LeafComponent):
    def __init__(self, position, dimensions, color):
        super().__init__(position)
        self._dimensions = dimensions
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def dimensions(self):
        return self._dimensions
