from src.Controller.controller_state.menu_state import MenuState
from src.Model.models.game_model import GameModel


class MenuGameState(MenuState):
    def __init__(self, controller):
        super().__init__(controller)
        controller.model = GameModel()

    def run(self):
        # self._eventObservable.publish(self.controller.view.getEvents())
        self.controller.view.draw(self.controller.model)
