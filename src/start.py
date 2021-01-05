from src.controller.gameFactory.creator.game_controller_factory import GameControllerCreator

game = GameControllerCreator(640, 480).createGameController()

game.run()
