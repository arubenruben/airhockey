from src.Model.drawables.drawable import Drawable


class Image(Drawable):
    def __init__(self, position, dimensions, filename):
        super().__init__(position)
        self._filename = filename
        self._dimensions = dimensions

    @property
    def filename(self):
        return self._filename

    @property
    def dimensions(self):
        return self._dimensions
