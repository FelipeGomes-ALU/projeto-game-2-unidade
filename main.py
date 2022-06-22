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
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if pygame.key.get_pressed()[K_a]:
                x = x - 5
        if pygame.key.get_pressed()[K_d]:
                x = x + 5
        if pygame.key.get_pressed()[K_w]:
                y = y - 5
        if pygame.key.get_pressed()[K_s]:
                y = y + 5

    pygame.draw.rect(tela,(240,0,0),(x,y,20,20))
    pygame.draw.circle(tela,(240,240,240),(400,400),3,00)

    pygame.display.update()