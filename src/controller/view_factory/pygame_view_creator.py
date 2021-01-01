import pygame

from src.controller.view_factory.view_creator import ViewCreator


class PygameViewCreator(ViewCreator):
    def __init__(self, width, height):
        ViewCreator.__init__(self, width, height)

    def createView(self):
        pygame.init()
        return pygame.display.set_mode((self.width, self.height))
