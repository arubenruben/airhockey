from src.model.drawables.concreteDrawables.player import Player
from src.model.drawables.genericDrawables.rectangle import Rectangle
from src.model.model import Model


class MainMenuModel(Model):

    def __init__(self):
        super().__init__()
        self.listDrawables.append(Rectangle(0, 0, 100, 100, 255, 0, 0))
