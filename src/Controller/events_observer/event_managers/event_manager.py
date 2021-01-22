from src.Controller.events_observer.observers.concrete_listeners.exit_listener import ExitListener
from src.Controller.events_observer.observers.concrete_listeners.mouse_listener import MouseListener
from src.Controller.events_observer.observers.concrete_listeners.time_listener import TimeListener
from src.View.events.concrete_events.mouse_events.mouse_event import MouseEvent
from src.View.events.concrete_events.quit_events.quit_event import QuitEvent
from src.View.events.concrete_events.time_events.time_event import TimeEvent


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
        elif isinstance(event, TimeEvent):
            return self.timeEventNotify(event)
        elif isinstance(event, QuitEvent):
            return self.quitEventNotify(event)

    #
    #
    #
    # Aux Methods
    def mouseEventNotify(self, mouseEvent):
        for subscriber in self._subscribers:
            if isinstance(subscriber, MouseListener):
                subscriber.update(mouseEvent)

    def timeEventNotify(self, timeEvent):
        for subscriber in self._subscribers:
            if isinstance(subscriber, TimeListener):
                subscriber.update(timeEvent)

    def quitEventNotify(self, quitEvent):
        for subscriber in self._subscribers:
            if isinstance(subscriber, ExitListener):
                subscriber.update(quitEvent)
