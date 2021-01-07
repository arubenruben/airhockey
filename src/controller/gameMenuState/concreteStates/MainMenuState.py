import pygame

from src.controller.gameMenuState.State import State


class MainMenuState(State):

    def __init__(self, mainMenuModel):
        super().__init__(mainMenuModel)

    def run(self, view):

        while True:
            # TODO: Change this dependency on Pygame

            ev = pygame.event.poll()

            if ev.type == pygame.QUIT:
                break

            view.draw(self.model)

            view.render()

        pygame.quit()
