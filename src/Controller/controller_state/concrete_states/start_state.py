from src.Controller.controller_state.concrete_states.game_state import GameState
from src.Controller.controller_state.controller_state import ControllerState
from src.View.events.concrete_events.mouse_events.mouse_event import MouseEvent


class StartState(ControllerState):

    def __init__(self, controller, eventObservable):
        super().__init__(controller)
        self._eventObservable = eventObservable
        self._eventObservable.subscribe(MouseEvent, controller.model.buttonPlay, self.changeToSGameState)
        self._eventObservable.subscribe(MouseEvent, controller.model.buttonExit, self.changeToExitState)

    def run(self):
        self._eventObservable.publish(self.controller.view.getEvents())
        self.controller.view.draw(self.controller.model)

    def changeToSGameState(self):
        self.controller.state = GameState(self.controller)
