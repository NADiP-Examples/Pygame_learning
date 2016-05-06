#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Пример взят отсюда: http://plambir.blogspot.ru/2010/02/4.html

import pygame

speed = 2

up = pygame.K_w
down = pygame.K_s
left = pygame.K_a
right = pygame.K_d

# Это плитка на полу, она постепенно превращается в белую.
class Tiles(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, group=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        # это значения зеленого канала в RGB
        self.color = 255
        self.image.fill((255, self.color, 255))
        # Добавляем спрайт в группу.
        self.add(group)

    # Здесь мы постепенно обесцвечиваем квадрат,
    # увеличиваем значение зеленого канала.
    def update(self, dt):
        fill = dt / 2.0
        self.color += int(fill)
        if self.color >= 255:
            self.color = 255
        self.image.fill((255, self.color, 255))


if __name__ == '__main__':
    pygame.init()

    display = pygame.display.set_mode((640, 480))

    clock = pygame.time.Clock()

    hero = pygame.sprite.Sprite()
    hero.image = pygame.Surface((16, 16))
    hero.image.fill((0, 0, 0))
    hero.rect = hero.image.get_rect()
    hero.rect.move_ip(16 * 18, 16 * 10)
    # Это группа спрайтов.
    group = pygame.sprite.Group()
    for x in range(640 // 16):
        for y in range(480 // 16):
            Tiles(x * 16, y * 16, group)

    done = False
    dt = 0
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
                continue
            if e.type == pygame.KEYDOWN \
                    and e.key == pygame.K_ESCAPE:
                done = True
                continue

        keys = pygame.key.get_pressed()
        if keys[up]:
            hero.rect.move_ip(0, -speed)
        if keys[down]:
            hero.rect.move_ip(0, speed)
        if keys[left]:
            hero.rect.move_ip(-speed, 0)
        if keys[right]:
            hero.rect.move_ip(speed, 0)

        # `pygame.sprite.spritecollide` находит все спрайты
        # из группы у которых есть столкновение со спрайтом,
        # в данном случае все плитки которых касается `hero`.
        for obj in pygame.sprite.spritecollide(hero, group, None):
            obj.color = 0

        # У всех спрайтах входящих в группу вызывается метод `update`.
        group.update(dt)

        display.fill((255, 255, 255))
        # Рисуем все спрайты из группы, используется поля спрайта
        # `image` и `rect`.
        group.draw(display)
        display.blit(hero.image, hero.rect)
        pygame.display.flip()

        dt = clock.tick(40)
