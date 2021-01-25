from src.Model.composite_drawables.composite_drawables.concreteComposite.sprites.sprite import Sprite
from src.Model.composite_drawables.leafs.concreteLeafs.rectangle import Rectangle
from src.Model.utils.dimensions import Dimensions
from src.Model.utils.position import Position


class Table(Sprite):
    def __init__(self, screenDimensions, wallThickness):
        super().__init__()
        self._screenDimensions = screenDimensions
        self._wallThickness = wallThickness
        self._leftWall = Rectangle(Position(0, 0), Dimensions(wallThickness, screenDimensions.height))
        self._rightWall = Rectangle(Position(screenDimensions.width - wallThickness, 0),
                                    Dimensions(wallThickness, screenDimensions.height))
        # self._bottomWall = Rectangle()
        # self._topWall = Rectangle()

    @property
    def leftWall(self):
        return self._leftWall

    @property
    def rightWall(self):
        return self._rightWall

    @property
    def topWall(self):
        return self._topWall

    @property
    def bottomWall(self):
        return self._bottomWall

    @property
    def wallThickness(self):
        return self._wallThickness
