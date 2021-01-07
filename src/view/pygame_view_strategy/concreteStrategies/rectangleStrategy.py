import pygame

from src.view.pygame_view_strategy.draw_strategy import DrawStrategy


class RectangleStrategy(DrawStrategy):
    def __init__(self, view):
        super().__init__(view)

    def draw(self, rectangle):
        pygame.draw.rect(self.view.screen, rectangle.color,
                         pygame.Rect(rectangle.xLeft, rectangle.yTop, rectangle.width, rectangle.height))
