import sys
import pygame
from Classes.Vector import Vector

FPS = 40
NORMAL = 0
TURN_LEFT = 1
TURN_RIGHT = 2
FORCE = 3
SLOW = 4


class Ship:
    def __init__(self, pos):
        self.pos = Vector(pos)
        self.image = pygame.Surface((50, 50))
        self.speed = Vector((0, 1))
        self.acsel = 0.05
        self.angle_speed = 3
        self.state = NORMAL
        self.draw()
        self.image = pygame.transform.rotate(self.image, 180)

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.state = TURN_LEFT
            elif event.key == pygame.K_RIGHT:
                self.state = TURN_RIGHT
            elif event.key == pygame.K_UP:
                self.state = FORCE
            elif event.key == pygame.K_DOWN:
                self.state = SLOW
        elif event.type == pygame.KEYUP:
            self.state = NORMAL

    def update(self):
        if self.state == TURN_LEFT:
            self.speed.rotate(-self.angle_speed)
        elif self.state == TURN_RIGHT:
            self.speed.rotate(self.angle_speed)
        elif self.state == FORCE:
            self.speed += self.speed.normalize()*self.acsel
        elif self.state == SLOW:
            self.speed -= self.speed.normalize()*self.acsel
        self.pos += self.speed
        print(self.speed.len())

    def draw(self):
        polygon = [(0, 25), (15, 20), (30, 10), (32, 10), (32, 20), (40, 20), (45, 17),
                   (45, 33), (40, 30), (32, 30), (32, 40), (30, 40), (15, 30), (0, 25)]
        pygame.draw.polygon(self.image, (0, 0, 220), polygon)

    def render(self, screen):
        rotate_image = pygame.transform.rotate(self.image, self.speed.angle)
        rect = rotate_image.get_rect(center=self.image.get_rect().center)
        rect.move_ip(self.pos.as_point())

        screen.blit(rotate_image, rect)
        pygame.draw.rect(screen, (200, 0, 0), rect, 1)

        # draw V Speed
        dx = self.image.get_rect().w/2
        dy = self.image.get_rect().h/2
        pygame.draw.line(screen, (0, 255, 0), (self.pos.x + dx, self.pos.y + dy),
                         ((self.pos + self.speed * 20).x + dx, (self.pos + self.speed * 20).y + dy))


if __name__ == "__main__":

    pygame.init()
    pygame.display.set_mode((800, 600))
    screen = pygame.display.get_surface()

    ship = Ship((20, 100))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            ship.events(event)
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(FPS)
        ship.update()
        screen.fill((0, 0, 0))
        ship.render(screen)
        pygame.display.flip()