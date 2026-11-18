import pygame
from os import path
from config import *

# tira o fundo preto das imagens e redimensiona elas
def monta_info():
    info = {}
    for n in range(1, NIVEL_MAXIMO + 1):
        nome, arquivo , escala = BASE [n - 1]
        imagem = pygame.image.load(path.join(IMG_DIR, arquivo)).convert()
        imagem.set_colorkey(0,0,0) # remove o preto do JPEG antes de redimensionar. Tivemos auxilio de IA
        tamanho = imagem.get_rect()
        largura = int(86 * escala)
        altura = int(largura * tamanho.bottom / tamanho.right)
        mini_altura = int(54 * tamanho.bottom / tamanho.right)
        info[n] = {
            "nome" : nome,
            "imagem": pygame.transform.scale(imagem,(largura, altura)),
            "mini" : pygame.transform.scale(imagem,(54, mini_altura)),
            "escala": escala
        }
        if n == NIVEL_MAXIMO:
            altura_vitoria = int(270 * tamanho.bottom / tamanho.right)
            info[n]["vitoria"] = pygame.transform.scale(imagem, (270, altura_vitoria))
    return info    