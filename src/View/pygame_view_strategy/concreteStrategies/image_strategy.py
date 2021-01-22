import pygame

from src.View.pygame_view_strategy.draw_strategy import DrawStrategy


class ImageStrategy(DrawStrategy):

    def draw(self, view, image):
        pygameImgType = pygame.image.load("../assets/" + str(image.filename))
        pygameImgTypeScaled = pygame.transform.scale(pygameImgType, (view.screenWidth, view.screenHeight))

        view.screenRender.blit(pygameImgTypeScaled, (image.position.xLeft, image.position.yTop))
