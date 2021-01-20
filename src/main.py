from src.Controller.controller import Controller
from src.Model.concrete_models.start_model import StartModel
from src.View.view_adapter.pygame_adapter import PygameAdapter


class Game:
    def __init__(self):
        self._view = PygameAdapter(800, 600)
        self._model = StartModel(self._view.width, self._view.height)
        self._controller = Controller(self._model, self._view)

    def start(self):
        self._controller.run()


Game().start()
