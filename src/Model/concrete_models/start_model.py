from collections import deque

from src.Model.drawables.concreteDrawables.button import Button
from src.Model.model import Model
from src.Model.utils.color import Color
from src.Model.utils.dimensions import Dimensions
from src.Model.utils.position import Position


class StartModel(Model):
    # TODO:Create A Model Factory
    def __init__(self, screenWidth, screenHeight):
        super().__init__(deque())
        self._screenWidth = screenWidth
        self._screenHeight = screenHeight
        self._buttonPlay = Button(Position(10, 10), Dimensions(100, 100), Color(255, 0, 0), "Ola", Color(0, 255, 255))
        self._buttonExit = Button(Position(10, 200), Dimensions(100, 100), Color(0, 255, 0), "Adeus", Color(0, 0, 255))

    @property
    def buttonPlay(self):
        return self._buttonPlay

    @property
    def buttonExit(self):
        return self._buttonExit

    @property
    def drawables(self):
        self._drawables.clear()

        self._drawables.append(self._buttonPlay)
        self._drawables.append(self._buttonExit)

        return self._drawables
