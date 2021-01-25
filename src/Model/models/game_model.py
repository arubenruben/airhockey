from src.Model.composite_drawables.composite_drawables.concreteComposite.sprites.concrete_sprites.table import Table
from src.Model.models.model import Model
from src.Model.utils.color import Color


class GameModel(Model):
    def __init__(self, screenDimensions):
        super().__init__()
        self._table = Table(screenDimensions, 10)
        self._background = Color(255, 0, 0)

    @property
    def drawables(self):
        self._drawables.clear()
        self._drawables.append(self._background)
        self._drawables.append(self._table)

        return self._drawables
