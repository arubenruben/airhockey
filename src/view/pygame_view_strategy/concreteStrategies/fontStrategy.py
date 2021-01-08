from src.view.pygame_view_strategy.draw_strategy import DrawStrategy


class FontStrategy(DrawStrategy):
    def __init__(self, view):
        super().__init__(view)

    def draw(self, string):
        pygameFontObject = self.view.font.render(string.stringToDraw, True, string.color)
        self.view.screen.blit(pygameFontObject, (string.xLeft, string.yTop))
