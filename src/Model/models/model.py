from collections import deque

from src.Model.utils.non_drawables.concrete_non_drawables.exit_button import ExitButton


class Model:
    def __init__(self):
        self._drawables = deque()
        self._exitButton = ExitButton()

    def drawables(self):
        pass

    @property
    def exitButton(self):
        return self._exitButton
