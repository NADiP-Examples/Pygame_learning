import pygame
from Classes.Base.RenderObject import RenderObject


class Circle(RenderObject):
    def __init__(self, pos=(0, 0), color=(255, 255, 255), size=(20, 20)):
        RenderObject.__init__(self, pos, size)
        self.draw_self(color)

    def draw_self(self, color):
        pygame.draw.circle(self.image, color, self.rect.center, self.rect.w//2)


class Bar(RenderObject):
    def __init__(self, pos=(0, 0), color=(255, 255, 255), size=(20, 20)):
        RenderObject.__init__(self, pos, size)
        self.draw_self(color)

    def draw_self(self, color):
        pygame.draw.rect(self.image, color, self.image.fill(color))