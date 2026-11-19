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




    

