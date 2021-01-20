class MenuState:
    def __init__(self, controller):
        self._controller = controller

    @property
    def controller(self):
        return self._controller

    def clickStart(self):
        pass

    def clickQuit(self):
        pass

    def run(self):
        pass
