class Image:
    def __init__(self, filename, x, y):
        self._filename = filename
        self._x = x
        self._y = y

    @property
    def filename(self):
        return self._filename

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
