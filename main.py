import pygame
import random

from pygame.locals import *

pygame.init()
# tela
bg = pygame.image.load('background.png')
largura = 720
altura = 680
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('star dust')
relogio = pygame.time.Clock()

# cores

verde = (0, 178, 14)
azul = (58, 53, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
branco = (255,255,255)
amarelo = (255, 255, 0)

# variaveis do jogo


colunas = 7
linhas = 6
bolax = random.randint(100,600)
fonte = pygame.font.SysFont('ArialBlack', 50)
pygame.mixer.init()
pygame.mixer.music.load('RUSH E editada.mp3')

pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# funções do jogo
pygame.font.SysFont('arial', 50)
pygame.time.set_timer(pygame.USEREVENT, 10000)
som_impacto = pygame.mixer.Sound('som_impacto.wav')
vol_imp = 1.5
def fundodetela():
    tela.blit(bg, (0, 0))
    Bola.desenhar(tela)
    for bloco in blocos:
        bloco.desenhar(tela)
    plataforma_Jogador.desenhar_plataforma(tela)

#  mapa externo

    pygame.draw.line(tela, preto, (0, largura), (0, 0), 10)
    pygame.draw.line(tela, preto, (0, 3), (720, 2), 10)
    pygame.draw.line(tela, preto, (largura, 1), (720, 680), 10)
    pygame.draw.line(tela, preto, (0, 680), (720, 680), 15)
# gameover
    if gameover == 'true':
        if len(blocos) == 0:
            texto = fonte.render("parabens!, você venceu", 1, (255, 255, 255))
        else:
            texto = fonte.render("que pena, você perdeu!", 1, (255, 255, 255))
        tela.blit(texto, ((largura // 2 - texto.get_width() // 2), altura // 2 - texto.get_height() // 2))


    pygame.display.update()

# objetos e funções
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
    def __init__(self, x, y, r, cor):
        self.x = x
        self.y = y
        self.r = r
        self.cor = cor
        self.vx = random.choice([ 3, -3])
        self.vy = -3

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, [self.x, self.y], self.r)

    def movimento(self):
        self.x += self.vx
        self.y += self.vy


class bloco(object):
    def __init__(self, x, y, l, a,cor):
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

class rebloco(object):
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
        for c in range(5):
            blocos.append(bloco(10 + l * 79, 15 + c * 35, 70, 25, verde))


init()
Bola = Bola(bolax, 550, 9, amarelo)
list_Bolas = [Bola]
plataforma_Jogador = plataforma(largura / 2, altura - 75, 20, 150, (vermelho))

gameover = 'false'

# core do jogo
while 'TRUE':
    relogio.tick(70)
    pygame.mouse.set_visible(bool(0))
    Bola.movimento()

# controle da plataforma
    if pygame.mouse.get_pos()[0] - plataforma_Jogador.l // 2 < 0:
        plataforma_Jogador.x = 0
    elif pygame.mouse.get_pos()[0] + plataforma_Jogador.l // 2 + 120 > largura:
        plataforma_Jogador.x = largura - plataforma_Jogador.l - 110
    else:
        plataforma_Jogador.x = pygame.mouse.get_pos()[0] - plataforma_Jogador.l

 # fisica da plataforma
    if (Bola.x >= plataforma_Jogador.x and Bola.x <= plataforma_Jogador.x + plataforma_Jogador.l ) or (Bola.x + Bola.r >= plataforma_Jogador.x and Bola.x + Bola.r <= plataforma_Jogador.x + plataforma_Jogador.l + 135):
        if (Bola.y >= plataforma_Jogador.y and Bola.y <= plataforma_Jogador.y + plataforma_Jogador.a) or (Bola.y + Bola.r >= plataforma_Jogador.y and Bola.y + Bola.r <= plataforma_Jogador.y + plataforma_Jogador.a-20):
           if Bola.y >= plataforma_Jogador.y:
                Bola.vy *= -1
                som_impacto.set_volume(vol_imp)
                som_impacto.play()

# fisica dos blocos
    for bloco in blocos:
        if (Bola.x >= bloco.x and Bola.x <= bloco.x + bloco.l) or Bola.x + Bola.r >= bloco.x and Bola.x + Bola.r <= bloco.x + bloco.l:
            if (Bola.y >= bloco.y and Bola.y <= bloco.y + bloco.a) or Bola.y + Bola.r >= bloco.y and Bola.y + Bola.r <= bloco.y + bloco.a:
                #bloco.visible = False
                blocos.pop(blocos.index(bloco))
                Bola.vy *=-1
                som_bloco = pygame.mixer.Sound('sombloco4.wav')
                som_bloco.set_volume(vol_imp)
                som_bloco.play()

 # fisica das paredes
    if Bola.x + Bola.r>= largura:
        Bola.vx *= -1
        som_impacto.set_volume(vol_imp)
        som_impacto.play()

    if Bola.x < 0:
        Bola.vx *= -1
        som_impacto.set_volume(vol_imp)
        som_impacto.play()

    if Bola.y<= 0:
        Bola.vy *=-1
        som_impacto.set_volume(vol_imp)
        som_impacto.play()

# sistema de aumento da velocidade
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            Bola.vx *= 1.2
            Bola.vy *= 1.2
# GameOver
    if Bola.y > 680 or len(blocos) == 0:
        gameover = 'true'
        Bola.vx = 0
        Bola.vy = 0
        pygame.mixer.music.stop()
        vol_imp = 0.0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        gameover = 'false'
        blocos.clear()
        for l in range(9):
            for c in range(5):
                blocos.append(rebloco(10 + l * 79, 15 + c * 35, 70, 25, verde))
        Bola.x = bolax
        Bola.y = 550
        Bola.vx = random.choice([ 3, -3])
        Bola.vy = -3
        pygame.mixer.music.play(1,0.0,0)
        vol_imp = 0.5


    fundodetela()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
