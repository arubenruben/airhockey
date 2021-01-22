from src.View.events.event import Event


class TimeEvent(Event):
    def __init__(self, lastTimeStamp, currentTimeStamp):
        self._lastTimeStamp = lastTimeStamp
        self._currentTimeStamp = currentTimeStamp

    @property
    def lastTimeStamp(self):
        return self._lastTimeStamp

    @property
    def currentTimeStamp(self):
        return self._currentTimeStamp
