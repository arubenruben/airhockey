from src.Model.drawables.concreteDrawables.button import Button
from src.Model.drawables.genericDrawables.font import Font
from src.Model.drawables.genericDrawables.image import Image
from src.Model.models.model import Model
from src.Model.utils.color import Color
from src.Model.utils.dimensions import Dimensions
from src.Model.utils.position import Position


class StartModel(Model):
    # TODO:Create A Model Factory
    def __init__(self, screenWidth, screenHeight):
        super().__init__()
        self._screenWidth = screenWidth
        self._screenHeight = screenHeight
        self._background = Image(Position(0, 0), Dimensions(screenWidth, screenHeight), "start-background.png")
        self._title = Font(Position(screenWidth * 0.35, screenHeight * 0.40), Color(255, 255, 255),
                           "Air Hockey.By Ruben Almeida")
        self._buttonPlay = Button(Position(screenWidth * 0.2, screenHeight * 0.45),
                                  Dimensions(screenWidth / 4, screenWidth / 8),
                                  Color(0, 255, 0), "Play",
                                  Color(255, 255, 255))
        self._buttonExit = Button(Position(screenWidth * 0.6, screenHeight * 0.45),
                                  Dimensions(screenWidth / 4, screenWidth / 8),
                                  Color(255, 0, 0), "Quit",
                                  Color(255, 255, 255))

    @property
    def buttonPlay(self):
        return self._buttonPlay

    @property
    def buttonExit(self):
        return self._buttonExit

    @property
    def drawables(self):
        self._drawables.clear()
        self._drawables.append(self._background)
        self._drawables.append(self._title)
        self._drawables.append(self._buttonPlay)
        self._drawables.append(self._buttonExit)

        return self._drawables
