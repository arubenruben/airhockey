class View:
    def __init__(self, width, height, screen):
        self._height = height
        self._width = width
        self._screen = screen

    @property
    def screen(self):
        return self._screen

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    def draw(self, model):
        pass

    def render(self):
        pass
