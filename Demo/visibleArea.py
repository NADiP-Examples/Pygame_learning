# from pygame import *
from Classes.PyMain import PyMain
from Classes.Collections import characters
from Classes.Collections.simple_objects import Bar


class PyVisible(PyMain):
    def __init__(self, hero, width=640, height=480):
        PyMain.__init__(self, width, height)
        self.hero = hero

    def render(self):
        for render_obj in self.render_list:
            hero_view_rect = self.hero.view_image.get_rect()
            hero_view_rect.center = self.hero.pos.as_point()
            if render_obj.rect.colliderect(hero_view_rect):
                render_obj.render(self.screen)



hero = characters.Circle(pos=(20, 40), color=(200, 50, 0))
game = PyVisible(hero)
bar1 = Bar(pos=(40, 20), color=(0, 50, 200))
bar2 = Bar(pos=(60, 120), color=(0, 50, 200))

game.add_render_object(hero)
game.add_render_object(bar1)
game.add_render_object(bar2)

game.mainloop(FPS=20)