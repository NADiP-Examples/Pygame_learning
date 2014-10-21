#import pygame, math
#from pygame.locals import *
#from Classes.Vector import Vector
from Classes.OutPutWindow import OutPutWindow
from Classes.Track import Create_Track
#from Utilities import load_image
from Classes.Car import Car
from Classes.Buttons import Button
from Classes.PyMain import PyMain
from Classes.Tire import Tire

def create_track():
    global new_track, mainWindow
    new_track = Create_Track()
    mainWindow.add_none_render_object(new_track)

def complete_track():
    global new_track, tires, mainWindow, car
    for point in new_track.points:
        tire = Tire(point)
        tires.append(tire)
        mainWindow.add_render_object(tire)
    car = Car((300,150),(30,0))
    car.add_track(tires)
    mainWindow.add_render_object(car)
    #print("Complete")
    #print(new_track.points)


mainWindow = PyMain(800,600)
#vector = Game_Object((200,120),(30,0))
car = None
new_track = None
tires = [] #Покрышки
button_create = Button(pos = (10,10),image_names =('button_off.png','button_hover.png','button_click.png'),
                    function=create_track, text='Create Track', w =120)
button_complete = Button(pos = (10,45),image_names =('button_off.png','button_hover.png','button_click.png'),
                    function=complete_track, text='Complete Track', w =120)

#mainWindow.add_render_object(car)

mainWindow.add_render_object(button_create)
mainWindow.add_render_object(button_complete)
mainWindow.MainLoop()