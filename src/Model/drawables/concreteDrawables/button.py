from src.Controller.events_observer.observers.concrete_listeners.mouse_listener import MouseListener
from src.Model.drawables.drawable import Drawable
from src.Model.utils.color import Color
from src.View.events.concrete_events.mouse_events.concrete_mouse_events.mouse_left_click_event import \
    MouseLeftClickEvent


class Button(Drawable, MouseListener):
    def __init__(self, position, dimensions, colorBackground, text="", textColor=Color(0, 0, 0)):
        Drawable.__init__(self, position)
        self._colorBackground = colorBackground
        self._dimensions = dimensions
        self._text = text
        self._textColor = textColor
        self._command = None

    def update(self, mouseEvent):
        if not isinstance(mouseEvent, MouseLeftClickEvent):
            return
        if mouseEvent.x < self.position.xLeft or mouseEvent.x > self.position.xLeft + self.dimensions.width:
            return
        if mouseEvent.y < self.position.yTop or mouseEvent.y > self.position.yTop + self.dimensions.height:
            return

        self._command.execute()

    #
    # Setter and Getters
    @property
    def colorBackground(self):
        return self._colorBackground

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        self._command = command

    @property
    def dimensions(self):
        return self._dimensions

    @property
    def text(self):
        return self._text

    @property
    def textColor(self):
        return self._textColor
