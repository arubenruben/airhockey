
from view import View

class ViewPygameAdapter(View):
    
    def __init__(self,width,height):
        View.__init__(self,width,height)


    def draw(self, element):
        print("Hello")
