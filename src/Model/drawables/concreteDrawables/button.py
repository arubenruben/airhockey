from src.Controller.events_observer.event_observer import EventObserver
from src.Model.drawables.drawable import Drawable
from src.Model.drawables.genericDrawables.font import Font
from src.Model.drawables.genericDrawables.rectangle import Rectangle
from src.Model.utils.position import Position


class Button(Drawable, EventObserver):
    def __init__(self, position, dimensions, colorBackground, text, colorText):
        Drawable.__init__(self, position)
        EventObserver.__init__(self)
        self._dimensions = dimensions
        self._colorBackground = colorBackground
        self._font = Font(
            Position((position.xLeft + dimensions.width / 2.0) * 0.6, (position.yTop + dimensions.height / 2.0) * 0.9),
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
