import pygame

from src.View.pygame_view_strategy.draw_strategy import DrawStrategy


class RectangleStrategy(DrawStrategy):

    def draw(self, view, rectangle):
        pygame.draw.rect(view.screenRender,
                         pygame.Color(rectangle.color.red, rectangle.color.green, rectangle.color.blue),
                         pygame.Rect(rectangle.position.xLeft, rectangle.position.yTop, rectangle.dimensions.width,
                                     rectangle.dimensions.height))
