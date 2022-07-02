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
vermelho = (255, 0, 0)
preto = (0, 0, 0)

# variaveis do jogo


colunas = 7
linhas = 6


# funções do jogo
def fundodetela():
    tela.blit(bg, (0, 0))
    Bola.desenhar(tela)
    for bloco in blocos:
        bloco.desenhar(tela)
    # plat_jogavel = pygame.draw.rect(tela, preto, (x, y, 60, 5))
    plataforma_Jogador.desenhar_plataforma(tela)
    pygame.display.update()

class plataforma(object):
    def __init__(self, x, y, l, a, cor):
        self.x = x
        self.y = y
        self.l = l
        self.a = a
        self.cor = cor

    def desenhar_plataforma(self, tela):
        pygame.draw.rect(tela, self.cor, [self.x, self.y, self.a, self.l])


class Bola(object):
    def __init__(self, x, y, l, a, cor):
        self.x = x
        self.y = y
        self.l = l
        self.a = a
        self.cor = cor
        self.vx = -3
        self.vy = -3

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, [self.x, self.y, self.a, self.l])

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


# gerador de blocos
blocos = []


def init():
    global blocos
    blocos = []
    for l in range(9):
        for c in range(9):
            blocos.append(bloco(10 + l * 79, 15 + c * 35, 70, 25, verde))


init()
Bola = Bola(400, 550, 20, 20, azul)
plataforma_Jogador = plataforma(largura / 2, altura - 75, 20, 140, (vermelho))

# core do jogo
while 'TRUE':
    relogio.tick(60)
    pygame.mouse.set_visible(bool(0))
    Bola.movimento()
    if pygame.mouse.get_pos()[0] - plataforma_Jogador.l // 2 < 0:
        plataforma_Jogador.x = 0
    elif pygame.mouse.get_pos()[0] + plataforma_Jogador.l // 2 + 120 > largura:
        plataforma_Jogador.x = largura - plataforma_Jogador.l - 110
    else:
        plataforma_Jogador.x = pygame.mouse.get_pos()[0] - plataforma_Jogador.l

 # fisica da plataforma
    if (Bola.x >= plataforma_Jogador.x and Bola.x <= plataforma_Jogador.x + plataforma_Jogador.l) or (
            Bola.x + Bola.l >= plataforma_Jogador.x and Bola.x + Bola.l <= plataforma_Jogador.x + plataforma_Jogador.l + 130):
        if Bola.y + Bola.a >= plataforma_Jogador.y and Bola.y + Bola.a <= plataforma_Jogador.y + plataforma_Jogador.a:
            Bola.vy *= -1

 # fisica das paredes
    if Bola.x + Bola.l >= largura:
        Bola.vx *= -1

    if Bola.x < 0:
        Bola.vx *= -1

    if Bola.y<= 0:
        Bola.vy *=-1



    fundodetela()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        # if pygame.key.get_pressed()[K_a]:
        #    x = x - 5
        # if pygame.key.get_pressed()[K_d]:
        #    x = x + 5



