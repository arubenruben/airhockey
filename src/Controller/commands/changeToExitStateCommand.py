from src.Controller.commands.command import Command


class ChangeToExitStateCommand(Command):
    def __init__(self, controller):
        super().__init__(controller)

    def execute(self):
        self._controller.menuState.changeToExitState()

    def undo(self):
        super().undo()
