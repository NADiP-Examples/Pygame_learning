# Коллекция классов персонажей
import pygame
from pygame import *
from Utilities.Vector import Vector


class Circle:
    def __init__(self, pos=(0, 0), color=(255, 255, 255), size=(20, 20)):
        self.image = pygame.Surface(size)
        self.pos = Vector(pos)
        self.draw_self(color)
        self.direction = None
        self.speed = 50
        self.directions = {K_LEFT: Vector((-self.speed, 0)),
                           K_RIGHT: Vector((self.speed, 0)),
                           K_UP: Vector((0, -self.speed)),
                           K_DOWN: Vector((0, self.speed)),
        }
        # Радиус зоны обзора
        self._view_radius = 50
        self.view_image = pygame.Surface((self.view_radius*2, self.view_radius*2), pygame.SRCALPHA)
        self.view_image.fill((100, 100, 100, 60))

    @property
    def view_radius(self):
        return self._view_radius

    @view_radius.setter
    def view_radius(self, value):
        self._view_radius = value
        self.view_image = pygame.Surface((self.view_radius*2, self.view_radius*2), pygame.SRCALPHA)
        self.view_image.fill((100, 100, 100, 60))

    @property
    def rect(self):
        rect = self.image.get_rect()
        rect.center = self.pos.as_point()
        return rect

    def draw_self(self, color):
        pygame.draw.circle(self.image, color, self.image.get_rect().center, self.rect.w // 2)

    def events(self, event):
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
                self.direction = event.key
        elif event.type == KEYUP:
            self.direction = None

    def move(self, dt):
        k_speed = dt/1000
        self.pos += self.directions[self.direction]*k_speed

    def update(self, dt=0):
        if self.direction:
            self.move(dt)

    def render(self, screen):
        view_rect = self.view_image.get_rect()
        view_rect.center = self.pos.as_point()
        screen.blit(self.view_image, view_rect)
        screen.blit(self.image, self.rect)
