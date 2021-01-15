from src.Controller.controller import Controller
from src.Model.concrete_models.start_model import StartModel
from src.View.view_adapter.pygame_adapter import PygameAdapter

view = PygameAdapter(800, 600)
model = StartModel(view.width, view.height)
controller = Controller(model, view)
controller.run()
