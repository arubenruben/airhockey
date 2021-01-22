class MenuState:
    def __init__(self, controller):
        self._controller = controller

    @property
    def controller(self):
        return self._controller

    def changeToSGameState(self):
        pass

    def changeToExitState(self):
        pass

    def run(self):
        pass
