from src.Model.composite_drawables.drawable import Drawable


class LeafComponent(Drawable):
    def __init__(self, position):
        self._position = position

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    def getDrawables(self, list):
        return list.append(self)
