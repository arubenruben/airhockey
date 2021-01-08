import pygame

from src.view.pygame_view_strategy.draw_strategy import DrawStrategy


class ImageStrategy(DrawStrategy):
    def __init__(self, view):
        super().__init__(view)

    def draw(self, image):
        pygameImgType = pygame.image.load("./assets/" + str(image.filename))
        self.view.screen.blit(pygameImgType, (image.x, image.y))
