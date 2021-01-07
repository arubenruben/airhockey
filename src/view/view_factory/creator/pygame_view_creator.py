from src.view.view_factory.creator.view_creator import ViewCreator
from src.view.view_factory.product.pygame_view import PygameView


class PygameViewCreator(ViewCreator):

    def create(self, screenWidth, screenHeight):
        return PygameView(screenWidth,screenHeight)
