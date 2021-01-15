from src.Controller.controller_state.concrete_states.start_state import StartState
from src.Controller.events_observer.concrete_observables.game_start_observable import GameStartObservable


class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._state = StartState(self, GameStartObservable(self._model))
        self._running = True

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        return

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model
        return

    @property
    def view(self):
        return self._view

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, running):
        self._running = running

    def run(self):
        while self.running:
            self._state.run()
        self.view.exit()
