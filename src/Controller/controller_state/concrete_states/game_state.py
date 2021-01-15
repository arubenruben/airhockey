from src.Controller.controller_state.controller_state import ControllerState
from src.Model.concrete_models.game_model import GameModel


class GameState(ControllerState):
    def __init__(self, controller):
        super().__init__(controller)
        controller.model = GameModel()

    def run(self):
        # self._eventObservable.publish(self.controller.view.getEvents())
        self.controller.view.draw(self.controller.model)
