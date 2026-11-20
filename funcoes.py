import pygame 
import random
from config import *
from assets import *

pygame.init()
pygame.mixer.init()


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DinoEvolution")

# Calcula o valor de um ovo: 1, 2, 4, 8... 20 conforme o nivel do dino.
def valor_ovo(n):
    a = 2 ** (n - 1)
    return a

# Mantem o preco do grupo; o nivel 1 usa a posicao zero da lista.
def preco_dino(n, lista_de_dinossauro):
    
    return 10 * valor_ovo(n) + 30 * lista_de_dinossauro[n - 1]

def compra_dino(n, lista_de_dinossauro):
    #Registra uma compra. A Partida so chama depois de conferir o saldo.
    lista_de_dinossauro[n - 1] += 1

def dinheiro(n):
    #Abrevia o dinheiro usando comparacoes, int, str e contas simples. 1k 1M 1B#
    if n >= 1000000000000:
        return str(int(n / 1000000000000)) + "T"
    elif n >= 1000000000:
        return str(int(n / 1000000000)) + "B"
    elif n >= 1000000:
        return str(int(n / 1000000)) + "M"
    elif n >= 1000:
        return str(int(n / 1000)) + "k"
    return str(int(n))

def itens_do_jogo(itens):
    lista = []
    for item in itens:
        lista.append(item)
    return lista

# ela verifica se o curso esta dentro da area
def dentro(cursor, area):
    x , y = cursor
    ax, ay, largura , altura = area
    if ax <= x <= ax + largura and ay <= y <= ay + altura:
        return True
    else:
        return False

# com ela verica se clicou em algo existente tipo: ovo, outro dino e asim por diante...
def distancia_dos_pontos(x1 , y1, x2, y2):
    dis = ((x1 - x2 )**2 + (y1 - y2)**2) ** 0.5
    return dis

# Ordena os dinos pela base (rect.bottom) para dar nocao de profundidade.Essa função organiza os dinossauros pela posição da parte de baixo deles na tela (rect.bottom). Ela compara os dinossauros vizinhos e troca a ordem quando necessário. Assim, ao desenhar seguindo essa lista, os que estão mais embaixo aparecem na frente dos que estão mais acima, criando uma sensação de profundidade.
def ordenar_dinos(itens):
    lista = itens_do_jogo(itens)
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j].rect.bottom > lista[j + 1].rect.bottom:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#Evita ultrapassar vinte dinos e entregas somados.
def tem_espaco(self):
        return self.ocupados() < MAX_DINOS

class Dino(pygame.sprite.Sprite):
    # cria um dino no campo com um nivel, pos, e hora
    def __init__(self, nivel, x , y,assets):
        pygame.sprite.Sprite.__init__(self)
        self.nivel = nivel
        self.image = assets["dinos"][nivel]["imagem"]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.x = self.rect.x
        self.y = self.rect.y
        self.vx = 0
        self.vy = 0
        self.tempo_direcao = 0
        self.tempo_ovo = random(OVO_MIN, OVO_MAX) * 1000
        self.preso = False
        self.escolher_direcao()





    

