from src.Model.composite_drawables.composite_drawables.concreteComposite.button import Button
from src.Model.composite_drawables.leafs.concreteLeafs.font import Font
from src.Model.composite_drawables.leafs.concreteLeafs.image import Image
from src.Model.models.model import Model
from src.Model.utils.color import Color
from src.Model.utils.dimensions import Dimensions
from src.Model.utils.position import Position


class StartModel(Model):
    # TODO:Create A Model Factory
    def __init__(self, screenDimensions):
        super().__init__()
        self._background = Image(Position(0, 0), screenDimensions, "start-background.png")
        self._title = Font(Position(screenDimensions.width * 0.35, screenDimensions.height * 0.40),
                           "Air Hockey.By Ruben Almeida", Color(255, 255, 255))
        self._buttonPlay = Button(Position(screenDimensions.width * 0.2, screenDimensions.height * 0.45),
                                  Dimensions(screenDimensions.width / 4, screenDimensions.width / 12),
                                  Color(0, 255, 0), "Play",
                                  Color(255, 255, 255))
        self._buttonExit = Button(Position(screenDimensions.width * 0.6, screenDimensions.height * 0.45),
                                  Dimensions(screenDimensions.width / 4, screenDimensions.width / 12),
                                  Color(255, 0, 0), "Quit",
                                  Color(255, 255, 255))

    @property
    def buttonPlay(self):
        return self._buttonPlay

    @property
    def buttonExit(self):
        return self._buttonExit

    def getDrawables(self):
        self._drawables.clear()

        self._background.getDrawables(self._drawables)
        self._title.getDrawables(self._drawables)
        self._buttonPlay.getDrawables(self._drawables)
        self._buttonExit.getDrawables(self._drawables)

        return self._drawables
