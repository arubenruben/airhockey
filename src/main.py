from src.controller.gameFactory.creator.game_controller_factory import GameControllerCreator

game = GameControllerCreator().createGameController(640, 480)

game.run()
