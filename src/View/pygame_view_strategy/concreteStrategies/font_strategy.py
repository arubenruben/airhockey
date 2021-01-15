import pygame

from src.View.pygame_view_strategy.draw_strategy import DrawStrategy


class FontStrategy(DrawStrategy):

    def draw(self, view, font):
        view.screenRender.blit(
            view.fontRender.render(font.text, True, pygame.Color(font.color.red, font.color.green, font.color.blue)),
            (font.position.xLeft, font.position.yTop)
        )
