from src.Controller.events_observer.observers.concrete_listeners.exit_listener import ExitListener


class ExitButton(ExitListener):
    def __init__(self):
        self._command = None

    def update(self, event):
        self.command.execute()

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        self._command = command
