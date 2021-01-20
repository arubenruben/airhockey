from src.Controller.events_observer.observers.concrete_listeners.mouse_listener import MouseListener
from src.View.events.concrete_events.mouse_events.mouse_event import MouseEvent


class EventManager:

    def __init__(self):
        self._subscribers = []

    def attach(self, observer):
        self._subscribers.append(observer)

    def detach(self):
        pass

    def notify(self, event):
        if isinstance(event, MouseEvent):
            return self.mouseEventNotify(event)

    #
    #
    #
    # Aux Methods
    def mouseEventNotify(self, mouseEvent):
        for subscriber in self._subscribers:
            if isinstance(subscriber, MouseListener):
                subscriber.update(mouseEvent)
