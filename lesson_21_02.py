import pygame
import random

def processing_blocks():
    global blocks, circle, no_jump, vx_circle, vy_circle, cnt, x_circle, y_circle, W_B, H_B, W, WW
    
    no_jump = True

    for i in range(len(blocks) - 1, -1, -1):
        if blocks[i].colliderect(circle):
            if no_jump:
                #левый верхний угол
                if blocks[i].x > x_circle and blocks[i].y > y_circle:
                    if vx_circle < 0 and vy_circle > 0:
                        vy_circle *= -1
                    if vx_circle > 0 and vy_circle < 0:
                        vx_circle *= -1
                    if vx_circle > 0 and vy_circle > 0:
                        vx_circle *= -1
                        vy_circle *= -1
                #правый верхний угол
                elif blocks[i].x + W_B < x_circle and blocks[i].y > y_circle:
                    if vx_circle < 0 and vy_circle > 0:
                        vx_circle *= -1
                        vy_circle *= -1
                    if vx_circle > 0 and vy_circle < 0:
                        vy_circle *= -1
                    if vx_circle < 0 and vy_circle < 0:
                        vx_circle *= -1
                #правый нижний угол
                elif blocks[i].x + W_B < x_circle and blocks[i].y + H_B < y_circle:
                    if vx_circle < 0 and vy_circle < 0:
                        vx_circle *= -1
                        vy_circle *= -1
                    if vx_circle < 0 and vy_circle > 0:
                        vx_circle *= -1
                    if vx_circle > 0 and vy_circle < 0:
                        vy_circle *= -1
                #левый нижний угол
                elif blocks[i].x > x_circle and blocks[i].y + H_B < y_circle:
                    if vx_circle > 0 and vy_circle < 0:
                        vx_circle *= -1
                        vy_circle *= -1
                    if vx_circle > 0 and vy_circle > 0:
                        vx_circle *= -1
                    if vx_circle < 0 and vy_circle < 0:
                        vy_circle *= -1
                elif blocks[i].x <= x_circle and blocks[i].x + W_B >= x_circle:
                        vy_circle *= -1
                elif blocks[i].y <= y_circle and blocks[i].y + H_B >= y_circle:
                        vx_circle *= -1
                no_jump = False
            blocks.pop(i)
            cnt += 1
            blocks.append(pygame.draw.rect(screen, (0, 0, 0), ((random.randint(WW, W - WW - W_B), random.randint(WW, 200), W_B, H_B)), 0))

def reflection_wall():
    global blocks, circle, no_jump, vx_circle, vy_circle
    
    if x_circle >= W - WW - R_C or x_circle <= R_C + WW:
        vx_circle = vx_circle * (-1)
    if y_circle <= WW + R_C:
        vy_circle = vy_circle * (-1)


COLOR = (100, 100, 0)
W = 1000
H = 800
SIZE = (W, H)
FPS = 60
WW = 20
R_C = 15

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(SIZE)
screen.fill(COLOR)
pygame.display.set_caption("Моя игра")
pygame.draw.rect(screen, (0, 0, 0), (0, 0, W, H + WW), WW)

x_circle = W // 2
y_circle = H // 2 + 300
vx_circle = 0
vy_circle = 0

w_plat = 100
h_plat = 5
x_plat = W // 2 - w_plat // 2
y_plat = H // 2 + 300 + R_C + 1

W_B = 80
H_B = 30

pygame.draw.circle(screen, (255, 255, 255), (x_circle, y_circle), R_C)
pygame.draw.rect(screen, (0, 0, 0), (x_plat, y_plat, w_plat, h_plat), 0)

blocks = []
for i in range(5):
    blocks.append(pygame.draw.rect(screen, (0, 0, 0), ((W_B + 10) * i + 300, 150, W_B, H_B), 0))
print(blocks)  


running = True
loose = False
cnt = 0

pygame.font.init()
font_cnt = pygame.font.SysFont('Comic Sans MS', 20)
data = 'СЧЁТ:'
ts_2 = font_cnt.render(data + str(cnt), True, (255, 255, 255))
screen.blit(ts_2, (WW + 10, WW))

while running:
    pygame.time.wait(1000 // FPS)
    screen.fill(COLOR)
    for i in range(len(blocks)):
        pygame.draw.rect(screen, (0, 0, 0), blocks[i], 0)
    
    
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, W, H + WW), WW)
    circle = pygame.draw.circle(screen, (255, 255, 255), (x_circle, y_circle), R_C)
    
    processing_blocks()

    plat = pygame.draw.rect(screen, (0, 0, 0), (x_plat, y_plat, w_plat, h_plat), 0)

    reflection_wall()

    if plat.colliderect(circle):
        if(y_circle >= y_plat - R_C and y_circle + R_C <= y_plat + h_plat and x_circle >= x_plat and x_circle <= x_plat + w_plat):
            vy_circle = vy_circle * (-1)
            
    x_circle += vx_circle
    y_circle += vy_circle

    # Ввод процесса (события)
        
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            vx_circle = 5
            vy_circle = -5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if x_plat < W - w_plat - WW - 40:
                x_plat += 40
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if x_plat > WW + 40:
                x_plat -= 40
        
    ts_2 = font_cnt.render(data + str(cnt), True, (255, 255, 255))
    screen.blit(ts_2, (WW + 10, WW))
    pygame.display.flip()

    if (y_circle > H):
        running = False
        loose = True

running = True

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

