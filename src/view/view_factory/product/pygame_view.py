import pygame

from src.model.drawables.genericDrawables.image import Image
from src.model.drawables.genericDrawables.rectangle import Rectangle
from src.view.pygame_view_strategy.concreteStrategies.imageStrategy import ImageStrategy
from src.view.pygame_view_strategy.concreteStrategies.rectangleStrategy import RectangleStrategy
from src.view.view_factory.product.view import View


class PygameView(View):

    def __init__(self, width, height):
        pygame.init()
        super().__init__(width, height, pygame.display.set_mode([width, height]))

    def draw(self, model):

        for element in model.listDrawables:
            if isinstance(element, Rectangle):
                return RectangleStrategy(self).draw(element)
            elif isinstance(element, Image):
                return ImageStrategy(self).draw(element)

    def render(self):
        pygame.display.flip()
