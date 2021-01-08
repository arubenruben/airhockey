from src.model.drawables.genericDrawables.font import Font
from src.model.model import Model


class MainMenuModel(Model):

    def __init__(self):
        super().__init__()
        self.listDrawables.append(Font("Hello World", 0, 0, 255, 0, 0))
