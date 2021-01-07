from collections import deque


class Model:

    # Linked List for drawables
    def __init__(self):
        self._listDrawables = deque()

    @property
    def listDrawables(self):
        return self._listDrawables

    @listDrawables.setter
    def listDrawables(self, value):
        self._listDrawables = value
        return

    @listDrawables.deleter
    def listDrawables(self):
        del self._listDrawables
        return
