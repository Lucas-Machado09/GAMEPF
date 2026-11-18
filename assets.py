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

# imagnes do fundo, meteoro, dino e sons
def carregas_assets():
    assets = {}
    fundo = pygame.image.loud(path.join(IMG_DIR, FUNDO)).convert
    assets["fundo"] = pygame.transform.scale(fundo, (WIDTH,HEIGHT))
    meteoro = pygame.image.load(path.join(IMG_DIR,METEORO)).convert_alpha()
    tam_meteoro = meteoro.get_rect()
    larg_meteoro = 340
    alt_meteoro = int(larg_meteoro * tam_meteoro.bottom / tam_meteoro.right)
    assets["meteoro"] = pygame.transform.scale(meteoro , (larg_meteoro , alt_meteoro)) 
    assets["dinos"] = monta_info()
    assets["titulo"] = pygame.font.SysFont(None,62)
    assets["grande"] = pygame.font.SysFont(None,36)
    assets["fonte"] = pygame.font.SysFont(None,26)
    assets["pequena"] = pygame.font.SysFont(None,21)
    assets["ovo"] = pygame.font.SysFont(None,37)

    som_encaixe = pygame.mixer.Sound(path.join(SND_DIR, "encaixe.wav"))
    for nome in ["coletar", "mesclar, comprar", "vitoria", "encaixe"]:
        assets[nome] = som_encaixe
    
    pygame.mixer.music.load(path.join(SND_DIR, MUSICA))
    pygame.mixer.music.set_volume(0.4)
    return assets