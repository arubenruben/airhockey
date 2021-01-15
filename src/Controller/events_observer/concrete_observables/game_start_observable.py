from src.Controller.events_observer.event_observable import EventObservable
from src.View.events.concrete_events.mouse_events.mouse_event import MouseEvent


class GameStartObservable(EventObservable):
    def __init__(self, model):
        super().__init__(model)

    def publish(self, eventList):
        for event in eventList:
            if isinstance(event, MouseEvent):
                self.mouseEvent(event)
