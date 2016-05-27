import pygame
from Utilities.Vector import Vector


class RenderObject:
    def __init__(self, pos=(0, 0), size=(20, 20)):
        self.image = pygame.Surface(size)
        self.pos = Vector(pos)

    @property
    def rect(self):
        rect = self.image.get_rect()
        rect.center = self.pos.as_point()
        return rect

    def events(self, event):
        pass

    def update(self, dt=0):
        pass

    def render(self, screen):
        screen.blit(self.image, self.rect)