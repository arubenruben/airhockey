class View:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def draw(self, model):
        pass

    def getEvents(self):
        pass

    def exit(self):
        pass
