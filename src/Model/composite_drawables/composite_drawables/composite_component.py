from src.Model.composite_drawables.drawable import Drawable


class CompositeComponent(Drawable):
    def __init__(self):
        self._drawables = []

    @property
    def drawables(self):
        return self._drawables

    def getDrawables(self, list):
        for element in self._drawables:
            element.getDrawables(list)
