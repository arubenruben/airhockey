import pygame

from src.view.view_factory.creator.view_creator import ViewCreator


class PygameViewCreator(ViewCreator):

    def create(self, screenWidth, screenHeight):
        return pygame.display.set_mode([screenWidth, screenHeight])
