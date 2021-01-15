from src.View.events.concrete_events.mouse_events.mouse_event import MouseEvent


class EventObservable:
    def __init__(self, model):
        self._model = model
        self._mouseSubscribers = []
        self._keyboardSubscribers = []
        self._exitSubscribers = []

    def publish(self, eventList):
        pass

    def subscribe(self, eventType, subscriber, action):
        if eventType is MouseEvent:
            self._mouseSubscribers.append(subscriber)
            subscriber.action = action

    def mouseEvent(self, event):
        for mouseSubscriber in self._mouseSubscribers:
            mouseSubscriber.update(event)

    def keyboardEvent(self, event):
        for keyboardSubscriber in self._keyboardSubscribers:
            keyboardSubscriber.update(event)

    def exitSubscriber(self, event):
        pass
