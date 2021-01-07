from src.model.drawables.drawable import Drawable


class Rectangle(Drawable):
    def __init__(self, xLeft, yTop, width, height, colorRed, colorGreen, colorBlue):
        self._xLeft = xLeft
        self._yTop = yTop
        self._width = width
        self._height = height
        self._color = (colorRed, colorGreen, colorBlue)

    @property
    def xLeft(self):
        return self._xLeft

    @property
    def yTop(self):
        return self._yTop

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def color(self):
        return self._color
