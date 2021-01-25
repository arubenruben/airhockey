from src.Controller.events_observer.observers.concrete_listeners.mouse_listener import MouseListener
from src.Model.composite_drawables.composite_drawables.composite_component import CompositeComponent
from src.Model.composite_drawables.leafs.concreteLeafs.rectangle import Rectangle
from src.View.events.concrete_events.mouse_events.concrete_mouse_events.mouse_left_click_event import \
    MouseLeftClickEvent


class Button(CompositeComponent, MouseListener):
    def __init__(self, position, dimensions, colorBackground, text=None, textColor=None):
        CompositeComponent.__init__(self)
        MouseListener.__init__(self)

        self._position = position
        self._colorBackground = colorBackground
        self._dimensions = dimensions
        self._command = None
        self.drawables.append(Rectangle(position, dimensions, colorBackground))
        self._font = None

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
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

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
