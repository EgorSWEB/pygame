import pygame
import random

"""
mat = [
[1,3],
[2, 22],
[1, 3]
]
mat[1][1]
"""
class Cell:
    bomb = False
    close = True
    flag = False
    numb = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
COUNT = 10
W_C = 45
INDENT = 5

COLOR = (51, 253, 255)

W = 1000
H = 800
SIZE = (W, H)
FPS = 60
SPACE = W // 4


field = []
for i in range(COUNT):
    row = []
    for j in range(COUNT):
        row.append(Cell(SPACE + j * (W_C + INDENT), SPACE + i * (W_C + INDENT)))
    field.append(row)


pygame.init()


screen = pygame.display.set_mode(SIZE)

loose = False
running = True

while running:
    pygame.time.wait(1000 // FPS)
    screen.fill(COLOR)

    for i in range(COUNT):
        for j in range(COUNT):
            pygame.draw.rect(screen, (120, 50, 0), (field[i][j].x, field[i][j].y, W_C, W_C), 0)
        
    
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

if loose:
    font = pygame.font.SysFont('Comic Sans MS', 100)
# Шрифт Comic Sans MS, размер 15
    data = 'GAME OVER'
    ts_1 = font.render(data, True, (255, 255, 255))
    screen.fill((255, 0, 0))
    screen.blit(ts_1, (W // 5, H // 3 + 50))
    while running:
        pygame.time.wait(1000 // FPS)
        
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()
        
pygame.quit()

