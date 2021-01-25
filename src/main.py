from src.Controller.controller import Controller
from src.Model.models.start_model import StartModel
from src.Model.utils.dimensions import Dimensions
from src.View.view_adapter.pygame_adapter import PygameAdapter


class Game:
    def __init__(self):
        screenDimensions = Dimensions(800, 600)
        self._view = PygameAdapter(screenDimensions, 30)
        self._model = StartModel(screenDimensions)
        self._controller = Controller(self._model, self._view)

    def start(self):
        self._controller.run()


Game().start()
