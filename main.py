import pygame

from pygame.locals import *

pygame.init()

tela = pygame.display.set_mode((900,600))
pygame.display.set_caption('star dust')
relogio = pygame.time.Clock()

largura = 1000
altura = 800
x = largura/2
y = altura/2

while 'true':
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if pygame.key.get_pressed()[K_a]:
                x = x - 20
        if pygame.key.get_pressed()[K_d]:
                x = x + 20
        if pygame.key.get_pressed()[K_w]:
                y = y - 20
        if pygame.key.get_pressed()[K_s]:
                y = y + 20

    pygame.draw.rect(tela,(240,0,0),(x,y,50,50))


    pygame.display.update()