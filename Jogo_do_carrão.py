import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()
pygame.mixer.music.set_volume(0.1)
bgm = pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(-1)

fart = pygame.mixer.Sound('sfx.mp3')

l = 640
a = 480
x = int(l/2)
y = int(a/2)
x_cntrl = 10
y_cntrl = 0
xb = random.randint(40, 600)
yb = random.randint(40, 440)
rlg = pygame.time.Clock()
batimentos = 0
font = pygame.font.SysFont('arial', 40, False, False)
dead = False

scr = pygame.display.set_mode((l, a))
pygame.display.set_caption('Jogo do carrão')
body_list = []
comp_s = 5


def solid_snake(body_list):
    for segment in body_list:
        pygame.draw.rect(scr, (50, 50, 50), (segment[0], segment[1], 20, 20))
def restart():
    global batimentos, comp_s, x, y, xb, yb, dead, head_list, body_list
    batimentos = 0
    comp_s = 5
    x =int(l/2)
    y =int(a/2)
    head_list = []
    body_list = []
    xb = random.randint(40, 600)
    yb = random.randint(40, 440)
    dead = False

while True:
    rlg.tick(30)
    scr.fill((150, 150, 150))
    msg = f'Pontos:{batimentos}'
    txt_f = font.render(msg, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                if y_cntrl == 10:
                    pass
                else:
                    y_cntrl = -10
                    x_cntrl = 0
            if event.key == K_a:
                if x_cntrl == 10:
                    pass
                else:
                    x_cntrl = -10
                    y_cntrl = 0
            if event.key == K_s:
                if y_cntrl == -10:
                    pass
                else:
                    y_cntrl = 10
                    x_cntrl = 0
            if event.key == K_d:
                if x_cntrl == -10:
                    pass
                else:
                    x_cntrl = 10
                    y_cntrl = 0

    x = x + x_cntrl
    y = y + y_cntrl

    if x >= 620:
        x = 20 
              
    if x <= 0:
        x = 620
    if y >= 460:
        y = 20
    if y <= 0:
        y = 460

    vermei = pygame.draw.rect(scr, (255, 0, 0), (xb, yb, 20, 20))
    verde = pygame.draw.rect(scr, (0, 255, 0), (x, y, 20, 20))

    if verde.colliderect(vermei):
        xb = random.randint(40, 600)
        yb = random.randint(40, 440)
        batimentos += 1
        fart.play()
        comp_s += 1

    head_list = []
    head_list.append(x)
    head_list.append(y)

    body_list.append(head_list)
    if body_list.count(head_list) > 1:
        scndf = pygame.font.SysFont('arial', 20, False, False)
        scndtxt = 'Você morreu! Aperte "e" para recomeçar'
        scndtxtf = scndf.render(scndtxt, True, (0,0,0))
        dead = True
        while dead:
            scr.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_e:  
                        restart()
                      
            scr.blit(scndtxtf, (40, a//2))            
            pygame.display.update()
    if len(body_list) > comp_s:
        del body_list[0]

    solid_snake(body_list)

    scr.blit(txt_f, (400, 40))

    pygame.display.update()