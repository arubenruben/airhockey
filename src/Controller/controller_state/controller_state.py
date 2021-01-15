class ControllerState:
    def __init__(self, controller):
        self._controller = controller

    @property
    def controller(self):
        return self._controller

    def run(self):
        pass

    # TODO: State de saida FAZER PARA FICAR CODIGO LIMPO
    def changeToExitState(self):
        pass
