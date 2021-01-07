class State:

    def __init__(self, model):
        self._model = model

    @property
    def model(self):
        return self._model

    def run(self, view):
        pass
