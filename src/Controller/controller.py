from time import time, sleep

from src.Controller.commands.changeToExitStateCommand import ChangeToExitStateCommand
from src.Controller.controller_state.concrete_states.start_state.start_state import MenuStartState


class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._menuState = MenuStartState(self)
        self._running = True

    def run(self):
        frameRate = 60
        frameTime = 1 / frameRate

        nextTimeStamp = self.getCurrentTimeStampInMilli()

        while self.running:

            currentTimeStamp = self.getCurrentTimeStampInMilli()

            if nextTimeStamp < currentTimeStamp:
                self._menuState.run()
                nextTimeStamp = self.getCurrentTimeStampInMilli() + frameTime
            else:
                sleep((nextTimeStamp - currentTimeStamp) / 1000)

        self.view.exit()

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

    @property
    def menuState(self):
        return self._menuState

    def getCurrentTimeStampInMilli(self):
        return int(time() * 1000)
