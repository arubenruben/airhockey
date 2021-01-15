from collections import deque


class Model:
    def __init__(self):
        self._drawables = deque()

    @property
    def drawables(self):
        return self._drawables
