from src.View.pygame_view_strategy.concreteStrategies.font_strategy import FontStrategy
from src.View.pygame_view_strategy.concreteStrategies.rectangle_strategy import RectangleStrategy
from src.View.pygame_view_strategy.draw_strategy import DrawStrategy


class ButtonStrategy(DrawStrategy):

    def draw(self, view, button):
        fontStrategy = FontStrategy()
        rectangleStrategy = RectangleStrategy()

        rectangleStrategy.draw(view, button.rectangle())
        fontStrategy.draw(view, button.font)
