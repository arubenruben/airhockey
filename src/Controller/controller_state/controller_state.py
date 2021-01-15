class ControllerState:
    def __init__(self, controller):
        self._controller = controller

    @property
    def controller(self):
        return self._controller

    def run(self):
        pass

    def changeToExitState(self):
        self.controller.running = False
