from src.View.events.concrete_events.mouse_events.mouse_event import MouseEvent


class MouseRightClick(MouseEvent):
    def __init__(self, x, y):
        super().__init__(x, y)
