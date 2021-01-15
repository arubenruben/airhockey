class Model:
    def __init__(self, drawables):
        self._drawables = drawables

    @property
    def drawables(self):
        return self._drawables
