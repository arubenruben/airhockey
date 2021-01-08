from src.model.drawables.concreteDrawables.player import Player
from src.model.drawables.genericDrawables.image import Image
from src.model.drawables.genericDrawables.rectangle import Rectangle
from src.model.model import Model


class MainMenuModel(Model):

    def __init__(self):
        super().__init__()
        self.listDrawables.append(Image("background.jpg", 0, 0))
