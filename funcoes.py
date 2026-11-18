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

# Mantem o preco do grupo; o nivel 1 usa a posicao zero da lista."""
def preco_dino(n, lista_de_dinossauro):
    #Mantem o preco do grupo; o nivel 1 usa a posicao zero da lista.
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
def montar_info():
    #Organiza os vinte niveis; carrega e dimensiona cada imagem uma vez.
    info = {}
    for n in range(1, NIVEL_MAXIMO + 1):
        nome, arquivo, escala = BASE[n - 1]
        imagem = pygame.image.load(path.join(IMG_DIR, arquivo)).convert()
        # EXTRA AUTORIZADO: remove o preto do JPEG antes de redimensionar. Tivemos auxilio de IA
        imagem.set_colorkey((0, 0, 0))
        tamanho = imagem.get_rect()
        # right e bottom de um get_rect() novo correspondem ao tamanho.
        # A proporcao original do JPEG e preservada.
        largura = int(86 * escala)
        altura = int(largura * tamanho.bottom / tamanho.right)
        mini_altura = int(54 * tamanho.bottom / tamanho.right)
        info[n] = {
            "nome": nome,
            "imagem": pygame.transform.scale(imagem, (largura, altura)),
            "mini": pygame.transform.scale(imagem, (54, mini_altura)),
            "escala": escala,
        }
        if n == NIVEL_MAXIMO:
            altura_vitoria = int(270 * tamanho.bottom / tamanho.right)
            info[n]["vitoria"] = pygame.transform.scale(imagem, (270, altura_vitoria))
    return info
