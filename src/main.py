from src.Controller.controller import Controller
from src.Model.models.start_model import StartModel
from src.View.view_adapter.pygame_adapter import PygameAdapter


class Game:
    def __init__(self):
        self._view = PygameAdapter(800, 600, 30)
        self._model = StartModel(self._view.screenWidth, self._view.screenHeight)
        self._controller = Controller(self._model, self._view)

    def start(self):
        self._controller.run()


Game().start()
