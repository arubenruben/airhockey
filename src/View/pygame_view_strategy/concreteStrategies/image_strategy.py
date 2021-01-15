import pygame

from src.View.pygame_view_strategy.draw_strategy import DrawStrategy


class ImageStrategy(DrawStrategy):

    def draw(self, view, image):
        pass
        pygameImgType = pygame.image.load("./assets/" + str(image.filename))
        view.screen.blit(pygameImgType, (image.x, image.y))
