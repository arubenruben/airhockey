class View:
    def __init__(self, screenWidth, screenHeight, fontSize):
        self._screenHeight = screenHeight
        self._screenWidth = screenWidth
        self._fontSize = fontSize

    @property
    def screenHeight(self):
        return self._screenHeight

    @property
    def screenWidth(self):
        return self._screenWidth

    def draw(self, model):
        pass

    def getEvents(self):
        pass

    def exit(self):
        pass

    def textDimensions(self, text):
        pass
