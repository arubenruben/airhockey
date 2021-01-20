from src.Controller.controller_state.concrete_states.game_state import GameState
from src.Controller.controller_state.menu_state import MenuState
from src.Controller.events_observer.event_managers.event_manager import EventManager


class StartState(MenuState):

    def __init__(self, controller):
        super().__init__(controller)
        self._eventManager = EventManager()
        self._eventManager.attach(self.controller.model.buttonPlay)
        self._eventManager.attach(self.controller.model.buttonExit)

    def run(self):
        for event in self.controller.view.getEvents():
            self._eventManager.notify(event)

        self.controller.view.draw(self.controller.model)

    def changeToSGameState(self):
        self.controller.state = GameState(self.controller)
