import pygame

from src.Model.drawables.concreteDrawables.button import Button
from src.Model.drawables.genericDrawables.font import Font
from src.Model.drawables.genericDrawables.image import Image
from src.Model.drawables.genericDrawables.rectangle import Rectangle
from src.Model.utils.dimensions import Dimensions
from src.View.events.concrete_events.mouse_events.concrete_mouse_events.mouse_left_click_event import \
    MouseLeftClickEvent
from src.View.events.concrete_events.quit_events.quit_event import QuitEvent
from src.View.pygame_view_strategy.concreteStrategies.button_strategy import ButtonStrategy
from src.View.pygame_view_strategy.concreteStrategies.font_strategy import FontStrategy
from src.View.pygame_view_strategy.concreteStrategies.image_strategy import ImageStrategy
from src.View.pygame_view_strategy.concreteStrategies.rectangle_strategy import RectangleStrategy
from src.View.view_adapter.view import View


class PygameAdapter(View):

    def __init__(self, width, height, fontSize):
        super().__init__(width, height, fontSize)
        pygame.init()
        pygame.font.init()
        self._screenRender = pygame.display.set_mode([width, height])
        self._fontRender = pygame.font.SysFont(None, fontSize)

    @property
    def screenRender(self):
        return self._screenRender

    @property
    def fontRender(self):
        return self._fontRender

    def draw(self, model):
        blackRGB = (0, 0, 0)

        self._screenRender.fill(blackRGB)

        allElements = model.drawables

        for element in allElements:
            if isinstance(element, Rectangle):
                RectangleStrategy().draw(self, element)
            elif isinstance(element, Image):
                ImageStrategy().draw(self, element)
            elif isinstance(element, Font):
                FontStrategy().draw(self, element)
            elif isinstance(element, Button):
                ButtonStrategy().draw(self, element)

        return pygame.display.flip()

    def getEvents(self):

        formattedEvents = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                formattedEvents.append(QuitEvent())
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                formattedEvents.append(MouseLeftClickEvent(event.pos[0], event.pos[1]))

        return formattedEvents

    def exit(self):
        pygame.quit()

    def textDimensions(self, text):
        return Dimensions(self._fontRender.size(text)[0], self._fontRender.size(text)[1])
