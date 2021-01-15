from src.Controller.controller import Controller
from src.Model.concrete_models.start_model import StartModel
from src.View.view_adapter.pygame_adapter import PygameAdapter

model = StartModel(640, 480)
view = PygameAdapter(640, 480)
controller = Controller(model, view)
controller.run()
