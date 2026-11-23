import pygame
from os import path
from config import *

# tira o fundo preto das imagens e redimensiona elas
def monta_info():
    info = {}
    for n in range(1, NIVEL_MAXIMO + 1):
        nome, arquivo , escala = BASE [n - 1]
        imagem = pygame.image.load(path.join(IMG_DIR, arquivo)).convert()
        imagem.set_colorkey((0,0,0)) # remove o preto do JPEG antes de redimensionar. Tivemos auxilio de IA
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
    fundo = pygame.image.load(path.join(IMG_DIR, FUNDO)).convert()
    assets["fundo"] = pygame.transform.scale(fundo, (WIDTH, HEIGHT))
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

# Desenha um poligono deslocado para (x, y) com escala k.
def poligono_local(tela, cor, pontos, x, y, k=1.0):   
    convertidos = []
    for px, py in pontos:
        convertidos.append((int(x + px * k), int(y + py * k)))
    pygame.draw.polygon(tela, cor, convertidos)

# Desenha um retangulo preenchido a partir de (x, y, largura, altura).
def retangulo(tela, cor, area):  
    x, y, largura, altura = area
    pontos = [(0, 0), (largura, 0), (largura, altura), (0, altura)]
    poligono_local(tela, cor, pontos, x, y)


# Desenha um botao ou painel 2D com sombra e relevo.
def placa(tela, area, cor, borda=(70, 42, 22)):  
    x, y, largura, altura = area
    retangulo(tela, (42, 26, 14), (x + 3, y + 4, largura, altura))
    retangulo(tela, borda, (x, y, largura, altura))
    retangulo(tela, cor, (x + 3, y + 3, largura - 6, altura - 6))
    clara = []
    escura = []
    for canal in cor:
        c1 = canal + 27
        if c1 > 255:
            c1 = 255
        c2 = canal - 24
        if c2 < 0:
            c2 = 0
        clara.append(c1)
        escura.append(c2)
    retangulo(tela, clara, (x + 3, y + 3, largura - 6, 3))
    retangulo(tela, escura, (x + 3, y + altura - 6, largura - 6, 3))

# Escreve texto com sombra na tela.
def escrever(tela, assets, texto, x, y, fonte="fonte", cor=(255, 250, 232), centro=False):  
    f = assets[fonte]
    sombra = f.render(str(texto), True, (42, 26, 14))
    superficie = f.render(str(texto), True, cor)
    r = superficie.get_rect()
    if centro:
        r.center = (int(x), int(y))
    else:
        r.topleft = (int(x), int(y))
    tela.blit(sombra, (r.x + 2, r.y + 2))
    tela.blit(superficie, r)

# Desenha uma elipse preenchida usando a tabela CIRCULO.
def oval(tela, cor, cx, cy, rx, ry):  
    pontos = []
    for px, py in CIRCULO:
        pontos.append((int(cx + rx * px / 1000), int(cy + ry * py / 1000)))
    pygame.draw.polygon(tela, cor, pontos)

# Desenha o contorno de uma elipse usando CIRCULO.
def anel(tela, cor, cx, cy, rx, ry, grossura=2):  
    pontos = []
    for px, py in CIRCULO:
        pontos.append((int(cx + rx * px / 1000), int(cy + ry * py / 1000)))
    pygame.draw.lines(tela, cor, True, pontos, grossura)

 # Desenha uma caixa de madeira de entrega centralizada em (x, y).
def desenhar_caixa(tela, x, y, k=1.0):  
    lado = int(42 * k)
    meio = int(lado / 2)
    oval(tela, (59, 43, 25), x, y + meio + 2, int(22 * k), int(6 * k))
    placa(tela, (x - meio, y - meio, lado, lado), (184, 128, 66), (92, 56, 26))
    poligono_local(tela, (132, 86, 40), [(-15, -12), (-11, -15), (15, 12), (11, 15)], x, y, k)
    poligono_local(tela, (132, 86, 40), [(11, -15), (15, -12), (-11, 15), (-15, 12)], x, y, k)

# Desenha um ovo manchado com sombra na posicao (x, y).
def desenhar_ovo(tela, x, y, k=1.0):  
    oval(tela, (59, 43, 25), x, y + int(13 * k), int(12 * k), int(4 * k))
    oval(tela, (250, 240, 206), x, y, int(11 * k), int(14 * k))
    anel(tela, (145, 114, 72), x, y, int(11 * k), int(14 * k), 2)
    oval(tela, (194, 152, 88), x - int(4 * k), y - int(3 * k), int(3 * k), int(4 * k))
    oval(tela, (194, 152, 88), x + int(4 * k), y + int(3 * k), int(2 * k), int(3 * k))

# Desenha uma moeda dourada na posicao (x, y).
def desenhar_moeda(tela, x, y, k=1.0):  
    raio = int(14 * k)
    pygame.draw.circle(tela, (153, 102, 24), (int(x), int(y)), raio)
    pygame.draw.circle(tela, (255, 214, 68), (int(x), int(y)), int(raio * 0.82))
    retangulo(tela, (214, 153, 36), (int(x - 2 * k), int(y - 6 * k), max(2, int(4 * k)), max(4, int(12 * k))))