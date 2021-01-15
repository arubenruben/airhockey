from src.Controller.events_observer.event_observer import EventObserver
from src.Model.drawables.drawable import Drawable
from src.Model.drawables.genericDrawables.font import Font
from src.Model.drawables.genericDrawables.rectangle import Rectangle
from src.Model.utils.position import Position
from src.View.events.concrete_events.mouse_events.concrete_mouse_events.mouse_left_click_event import MouseLeftClick


class Button(Drawable, EventObserver):
    def __init__(self, position, dimensions, colorBackground, text=None, colorText=None):
        Drawable.__init__(self, position)
        EventObserver.__init__(self)
        self._dimensions = dimensions
        self._colorBackground = colorBackground

        if text is not None and colorText is not None:
            self._font = Font(
                Position((position.xLeft + dimensions.width / 3.0),
                         (position.yTop + dimensions.height / 3.0)),
                colorText,
                text
            )

    @property
    def colorBackground(self):
        return self._colorBackground

    @property
    def font(self):
        return self._font

    def rectangle(self):
        return Rectangle(self.position, self.dimensions, self.colorBackground)

    @property
    def dimensions(self):
        return self._dimensions

    def update(self, event):

        if not isinstance(event, MouseLeftClick):
            return
        elif event.x < self.position.xLeft or event.x > self.position.xLeft + self.dimensions.width:
            return
        elif event.y < self.position.yTop or event.y > self.position.yTop + self.dimensions.height:
            return

        return self._action()
