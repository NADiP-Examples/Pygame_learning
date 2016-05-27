"""
Пример обработки нескольких одновременно нажатых клавиш
Про битовые операции читаем тут: http://younglinux.info/python/task/binary
"""
from Classes.PyMain import PyMain
from pygame import *


class Keys:
    def __init__(self):
        self.keys = [K_LEFT, K_RIGHT, K_UP, K_DOWN]
        # self.keys = [K_a, K_d, K_w, K_s]
        self.keys_state = 0b0000  # состояние нажатых клавиш в виде битов
        #  Каждый бит после 0b соответствует своей клавише
        #  Например, так выглядит маска для нажатых клавиш "влево-вверх": ob1010

    def events(self, event):
        if event.type == KEYUP or event.type == KEYDOWN:
            self.change_mask(event)
            print(event.key)

    def update(self, dt):
        """
        Пример использовани бинарной маски
        """
        # Суть маски - проверить только определенные(нужные в данный момент) биты, игнорировав остальные
        mask_left_right = 0b1100
        mask_left = 0b1000
        mask_right = 0b0100
        mask_up_down = 0b0011
        mask_up = 0b0010
        mask_down = 0b0001

        # Определем направление
        if self.keys_state & mask_left_right == mask_left_right:
            dir = "прямо"
        elif self.keys_state & mask_left == mask_left:
            dir = "влево"
        elif self.keys_state & mask_right == mask_right:
            dir = "вправо"
        else:
            dir = "прямо"

        # Определяем ускорение/торможение
        if self.keys_state & mask_up_down == mask_up_down:
            acceleration = "катимся"
        elif self.keys_state & mask_up == mask_up:
            acceleration = "газуем"
        elif self.keys_state & mask_down == mask_down:
            acceleration = "тормозим"
        else:
            acceleration = "катимся"

        print(dir, acceleration)

    def change_mask(self, event_key):
        """
        Изменяем маску в зависимости от нажатых/отпущенных клавиш
        :param event_key: событие клавиши
        """
        if event_key.key in self.keys:  # Обрабатываем только нужные клавиши
            if event_key.type == KEYDOWN:
                self.keys_state |= 0b1000 >> self.keys.index(event_key.key)
            if event_key.type == KEYUP:
                self.keys_state ^= 0b1000 >> self.keys.index(event_key.key)

        # Учтите: большинство обычных клавиатур не могут одновременно обрабатывать больше определенного кол-ва
        #         нажатых клавиш (это собенность работы контроллера клавиатуры)
        # Учтите: Маска 0b0010 отбражается на экране как 0b10. мы же не пишем 002, пишем 2
        print(bin(self.keys_state))


if __name__ == "__main__":
    main = PyMain(width=800, height=600)
    main.add_none_render_object(Keys())
    main.MainLoop(FPS=40)