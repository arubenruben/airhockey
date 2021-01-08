from src.model.drawables.drawable import Drawable


class Font(Drawable):

    def __init__(self, stringToDraw, xLeft, yTop, redValue, greenValue, blueValue):
        self._stringToDraw = stringToDraw
        self._xLeft = xLeft
        self._yTop = yTop
        self._color = (redValue, greenValue, blueValue)

    @property
    def stringToDraw(self):
        return self._stringToDraw

    @property
    def xLeft(self):
        return self._xLeft

    @property
    def yTop(self):
        return self._yTop

    @property
    def color(self):
        return self._color
