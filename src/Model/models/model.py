from collections import deque

from src.Model.non_drawables.concrete_non_drawables.exit_button import ExitButton


class Model:
    def __init__(self):
        self._drawables = deque()
        self._exitButton = ExitButton()

    @property
    def drawables(self):
        return self._drawables

    @property
    def exitButton(self):
        return self._exitButton
