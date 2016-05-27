from Classes.PyMain import PyMain
from Classes.Collections import characters
from Classes.Collections.simple_objects import Bar
from Utilities.Vector import Vector


class PyTargetCamera(PyMain):
    def __init__(self, hero, width=640, height=480):
        PyMain.__init__(self, width, height)
        self.hero = hero

    def change_coord_system(self, obj):
        """
        :return: вектор позиции объекта(obj) в системе координат героя(hero), который(герой) в центре экрана
        """
        return obj.pos+Vector(self.screen.get_rect().center) - self.hero.pos

    def render(self):
        self.screen.blit(self.hero.image, self.screen.get_rect().center)
        for render_obj in self.render_list:
            self.screen.blit(render_obj.image, self.change_coord_system(render_obj).as_point())


hero = characters.Circle(pos=(0, 0), color=(200, 50, 0), size=(20, 20))
hero.view_radius = 100
game = PyTargetCamera(hero)
bar1 = Bar(pos=(-40, 0), color=(0, 50, 200), size=(20, 20))
bar2 = Bar(pos=(60, 60), color=(0, 50, 200))

# game.add_render_object(hero)
game.add_render_object(bar1)
game.add_render_object(bar2)
game.add_none_render_object(hero)

game.mainloop(FPS=20)