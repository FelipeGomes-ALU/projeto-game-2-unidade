import pygame

from pygame.locals import *

pygame.init()
# tela
bg = pygame.image.load('background.png')
largura = 720
altura = 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('star dust')
relogio = pygame.time.Clock()

x = 325
y = 600
# cores
verde = (0, 178, 14)
azul = (58, 53, 255)
vermelho = (58, 53, 255)
preto = (0, 0, 0)

# variaveis do jogo


colunas = 7
linhas = 6



# funções do jogo
def fundodetela():
    tela.blit(bg,(0,0))
    Bola.desenhar(tela)
    for bloco in blocos:
        bloco.desenhar(tela)
    plat_jogavel = pygame.draw.rect(tela, preto, (x, y, 60, 5))



class Bola(object):
    def __init__(self,x,y,l,a,cor):
        self.x = x
        self.y = y
        self.l = l
        self.a = a
        self.cor = cor
        self.vx = 0
        self.vy = 5
    def desenhar(self,tela):
        pygame.draw.rect(tela,self.cor,[self.x, self.y, self.a, self.l])

    def movimento(self):
        self.x += self.vx
        self.y += self.vy


class bloco(object):
    def __init__(self, x, y, l, a, cor):
        self.x = x
        self.y = y
        self.l = l
        self.a = a
        self.cor = cor
        self.visivel = 'true'
        self.xx = self.x + self.l
        self.yy = self.y + self.a

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, [self.x, self.y, self.l, self.a])

#gerado de blocos
blocos = []
def init():
    global blocos
    blocos = []
    for l in range(9):
        for c in range(6):
            blocos.append(bloco(10 + l * 79, 50 + c * 35, 70, 25, verde))


init()
Bola = Bola(400,550,20,20,azul)

# core do jogo
while 'TRUE' :
    relogio.tick(60)



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if pygame.key.get_pressed()[K_a]:
            x = x - 5
        if pygame.key.get_pressed()[K_d]:
            x = x + 5
        fundodetela()


    pygame.display.update()

