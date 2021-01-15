class Position:
    def __init__(self, xLeft, yTop):
        self._xLeft = xLeft
        self._yTop = yTop

    @property
    def xLeft(self):
        return self._xLeft

    @property
    def yTop(self):
        return self._yTop
