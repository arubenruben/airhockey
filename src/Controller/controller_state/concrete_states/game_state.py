from src.Controller.controller_state.controller_state import ControllerState


class GameState(ControllerState):
    def __init__(self, controller):
        super().__init__(controller)

    def run(self):
        print("Ola")
