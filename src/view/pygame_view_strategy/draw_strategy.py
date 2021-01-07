class DrawStrategy:
    def __init__(self, view):
        self._view = view

    @property
    def view(self):
        return self._view

    def draw(self, drawable):
        pass
