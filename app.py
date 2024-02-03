import pygame as py
from classes import Button

py.init()

SIZE = (1280, 720)
COLOR = (100, 10, 34)
FPS = 120

screen = py.display.set_mode(SIZE)
screen.fill(COLOR)

button = Button(200, 100, 100, 100, 'Кнопка', screen)

running = True
while running:
    py.time.wait(1000 // FPS)

    for event in py.event.get():
        # check for closing window
        if event.type == py.QUIT:
            running = False

    button.update()
    py.display.flip()

py.quit()