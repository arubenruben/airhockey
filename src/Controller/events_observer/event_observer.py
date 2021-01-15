class EventObserver:
    def __init__(self, action=None):
        self._action = action

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action

    def update(self, event):
        return self._action()
