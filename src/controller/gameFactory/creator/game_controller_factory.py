from src.controller.gameFactory.product.game_controller import GameController
from src.controller.gameMenuState.concreteStates.MainMenuState import MainMenuState
from src.model.menus.main_menu_model import MainMenuModel
from src.view.view_factory.creator.pygame_view_creator import PygameViewCreator


class GameControllerCreator:

    def createGameController(self, screenHeight, screenWidth):
        gameView = PygameViewCreator().create(screenHeight, screenWidth)

        return GameController(MainMenuState(MainMenuModel()), gameView)
