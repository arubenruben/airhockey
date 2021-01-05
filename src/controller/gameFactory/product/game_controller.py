import pygame


class GameController:

    def __init__(self, gameModel, gameView):
        self.gameModel = gameModel
        self.gameView = gameView

    def run(self):
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
