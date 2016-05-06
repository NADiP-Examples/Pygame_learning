import os
import pygame


def load_image(name, path='Images', alpha_channel=False):
    fullname = os.path.join(path, name)

    image = pygame.image.load(fullname)  # Загружаем картинку и сохраняем поверхность (Surface)
    if alpha_channel:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image