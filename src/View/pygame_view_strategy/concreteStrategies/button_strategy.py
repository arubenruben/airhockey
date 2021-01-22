from src.Model.drawables.genericDrawables.font import Font
from src.Model.drawables.genericDrawables.rectangle import Rectangle
from src.Model.utils.position import Position
from src.View.pygame_view_strategy.concreteStrategies.font_strategy import FontStrategy
from src.View.pygame_view_strategy.concreteStrategies.rectangle_strategy import RectangleStrategy
from src.View.pygame_view_strategy.draw_strategy import DrawStrategy


class ButtonStrategy(DrawStrategy):

    def draw(self, view, button):
        rectangleStrategy = RectangleStrategy()
        fontStrategy = FontStrategy()

        textDimensions = view.textDimensions(button.text)

        rectangle = Rectangle(button.position, button.dimensions, button.colorBackground)

        font = Font(
            Position(button.position.xLeft + (rectangle.dimensions.width - textDimensions.width) / 2.0,
                     button.position.yTop + (rectangle.dimensions.height / 2.0 - textDimensions.height / 2.0)),
            button.textColor, button.text)

        rectangleStrategy.draw(view, rectangle)
        fontStrategy.draw(view, font)
