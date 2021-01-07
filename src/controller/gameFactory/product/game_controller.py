import pygame


class GameController:

    def __init__(self, menuState, gameView):
        self.menuState = menuState
        self.gameView = gameView

    def run(self):
        self.menuState.run(self.gameView)
