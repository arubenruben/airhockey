from src.Controller.commands.command import Command


class ChangeToGameStateCommand(Command):
    def __init__(self, controller):
        super().__init__(controller)

    def execute(self):
        self._controller.menuState.changeToSGameState()

    def undo(self):
        raise Exception()
