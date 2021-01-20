from src.Controller.controller_state.concrete_states.start_state import StartState
from src.Controller.events_observer.event_managers.event_manager import EventManager


class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._menuState = StartState(self)
        self._running = True

    def run(self):
        while self.running:
            self._menuState.run()

        self.view.exit()

    def clickStart(self):
        return self._menuState.clickStart()

    def clickQuit(self):
        return self._menuState.clickQuit()

    def changeState(self, newState):
        self._menuState = newState

    # Setter and Getters

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model
        return

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, running):
        self._running = running
        return

    @property
    def view(self):
        return self._view
