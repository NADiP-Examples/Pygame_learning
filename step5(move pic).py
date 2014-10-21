# -*- coding: utf-8 -*-
#Прежде чем переходить к следующему шагу, выполните 4 задания (Задания в коде в виде комментария)
import pygame, os
from pygame.locals import *

def load_image(name,alpha_cannel):
    fullname = os.path.join('Images', name) # Указываем путь к папке с картинками

    try:
        image = pygame.image.load(fullname) # Загружаем картинку и сохраняем поверхность (Surface)
    except (pygame.error): # Если картинки нет на месте
        print("Cannot load image:", name)
        return 0
    if(alpha_cannel):
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image

def move(event,x,y):
    print(event.key)
    #print("mod = ",event.mod)
    if event.key == 276:
        x = x-10
    #!Задание-3 Дописать функцию, для движения объекта во все 4 стороны
    return (x,y)

pygame.init() #инициализация
display = pygame.display.set_mode((400,400)) #создание окна
x = 50
y = 50

screen = pygame.display.get_surface() #определяем поверхность для рисования
#!Задание-2 Загрузить и отобразить на сцене ещё несколько произвольных картинок
image = load_image('skeleton.png',1) #загружаем картинку. Вторым аргументом указываем (есть/нет) альфа-канал

if image:
    done = False
else:
    done = True

while not done: #главный цикл программы
    for e in pygame.event.get(): #цикл обработки очереди событий окна
        if e.type == pygame.QUIT: #Обработка события "Закрытие окна"
            #!Задание-1 Дописать закрытие окна по нажатию клавиши Esc |"K_ESCAPE" - константа клавиши Esc
            done = True
        if (e.type == pygame.KEYDOWN): #Событие "Клавиша нажата"
            print('Key Down')
            x = x + 10
            #@uncomment-2 coords = move(e,x,y)
            #@uncomment-2 x = coords[0]
            #@uncomment-2 y = coords[1]

        if (e.type == pygame.KEYUP): #Событие "Клавиша отпущена"
            print('Key Up')
        if (e.type == pygame.MOUSEBUTTONDOWN): #Событие "Клавиша мыши нажата"
            print('Mouse Down')
            #!Задание-4 При нажатии кнопки "c" реализуйте изменение цвета фона по кругу (бирюзовый, розовый, черный, бирюзовый ...)
        #@uncomment-1 screen.fill((0,100,100))
    screen.blit(image,(x,y))  #отрисовываем содержимое поверхности image на поверхность screen
    pygame.display.flip()       #показываем на экране все что нарисовали на основной поверхности