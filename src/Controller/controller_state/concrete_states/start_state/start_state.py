from src.Controller.commands.changeToExitStateCommand import \
    ChangeToExitStateCommand
from src.Controller.controller_state.concrete_states.game_state.game_state import MenuGameState
from src.Controller.controller_state.concrete_states.start_state.commands.changeToGameState import \
    ChangeToGameStateCommand
from src.Controller.controller_state.menu_state import MenuState
from src.Controller.events_observer.event_managers.event_manager import EventManager


class MenuStartState(MenuState):

    def __init__(self, controller):
        super().__init__(controller)
        self._eventManager = EventManager()
        self._eventManager.attach(self.controller.model.buttonPlay)
        self._eventManager.attach(self.controller.model.buttonExit)
        self.controller.model.buttonPlay.command = ChangeToGameStateCommand(self.controller)
        self.controller.model.buttonExit.command = ChangeToExitStateCommand(self.controller)

        self._eventManager.attach(self.controller.model.exitButton)
        self.controller.model.exitButton.command = ChangeToExitStateCommand(self.controller)

    def run(self):
        for event in self.controller.view.getEvents():
            self._eventManager.notify(event)

        self.controller.view.draw(self.controller.model)

    def changeToSGameState(self):
        self.controller.state = MenuGameState(self.controller)

    def changeToExitState(self):
        self.controller.running = False
