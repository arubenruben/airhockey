from src.controller.gameFactory.product.game_controller import GameController
from src.model.game_model import GameModel
from src.view.view_factory.creator.pygame_view_creator import PygameViewCreator


class GameControllerCreator:

    def __init__(self, screenHeight, screenWidth):
        self.screenHeight = screenHeight
        self.screenWidth = screenWidth

    def createGameController(self):
        gameModel = GameModel()
        gameView = PygameViewCreator().create(self.screenHeight, self.screenWidth)

        return GameController(gameModel, gameView)
