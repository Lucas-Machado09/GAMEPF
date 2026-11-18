import pygame 
import random

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DinoEvolution")


FPS = 60

MAX_DINOS = 20

NIVEL_MAXIMO = 20

OVO_MIN, OVO_MAX = 6, 8

MEDIA_OVO = (OVO_MIN + OVO_MAX) / 2

VIDA_OVO = 12

MAX_OVOS = 40

ENTREGA_BASE = 12

ENTREGA_PASSO = 1

ENTREGA_MIN = 4

ENT_MAX = 8

QUAL_MAX = 12

COOLDOWN_ROLETA = 120

X_MIN, X_MAX = 12, WIDTH - 12

Y_MIN, Y_MAX = 310, HEIGHT - 60

FUNDO = "WhatsApp Image 2026-11-16 at 10.41.21.jpeg"

MUSICA = "dinosaur_extinction_old_classical_music_by_kris_klavenes_ending_soundtrack_05.02.2021.mp3"

BASE = [
    ("Baby", "dino_01.jpeg", 0.8),
    ("Velociraptor", "dino_02.jpeg", 0.9),
    ("Tricerátops", "dino_03.jpeg", 1.0),
    ("Estegossauro", "dino_04.jpeg", 1.1),
    ("Braquiossauro", "dino_05.jpeg", 1.1),
    ("Espinossauro", "dino_06.jpeg", 1.2),
    ("T-Rex", "dino_07.jpeg", 1.3),
    ("baby épico", "dino_08.jpeg", 0.8),
    ("Velociraptor épico", "dino_09.jpeg", 0.9),
    ("Tricerátops épico", "dino_10.jpeg", 1.0),
    ("Estegossauro épico", "dino_11.jpeg", 1.1),
    ("Braquiossauro épico", "dino_12.jpeg", 1.1),
    ("Espinossauro épico", "dino_13.jpeg", 1.2),
    ("T-Rex épico", "dino_14.jpeg", 1.3),
    ("baby gold", "dino_15.jpeg", 0.8),
    ("Velociraptor gold", "dino_16.jpeg", 0.9),
    ("Tricerátops gold", "dino_17.jpeg", 1.0),
    ("Estegossauro gold", "dino_18.jpeg", 1.1),
    ("Espinossauro gold", "dino_19.jpeg", 1.1),
    ("T-Rex gold", "dino_20.jpeg", 1.2),
]

PREMIOS = [("renda", 30), ("caixa", 0), ("renda", 60), ("caixa", 1),
           ("renda", 15), ("caixa", 0), ("renda", 120), ("caixa", 2)]

ROTULOS = ["+30s", "Caixa", "+60s", "Caixa +1", "+15s", "Caixa", "+2min", "Caixa +2"]

PESOS = [30, 20, 20, 8, 30, 20, 4, 2]

BRANCO = (245, 244, 231)

ESCURO = (18, 29, 29)

PAINEL = (27, 45, 43)

VERDE = (92, 205, 145)

DOURADO = (255, 207, 93)

CINZA = (172, 192, 181)

VERMELHO = (255, 140, 121)

# ==================== FUNCOES AUXILIARES ====================
def valor_ovo(n):
    """Calcula o valor de um ovo: 1, 2, 4, 8... conforme o nivel do dino."""
    return 2 ** (n - 1)

def preco_dino(n, lista_de_dinossauro):
    """Mantem o preco do grupo; o nivel 1 usa a posicao zero da lista."""
    return 10 * valor_ovo(n) + 30 * lista_de_dinossauro[n - 1]

def compra_dino(n, lista_de_dinossauro):
    """Registra uma compra. A Partida so chama depois de conferir o saldo."""
    lista_de_dinossauro[n - 1] += 1

def dinheiro(n):
    """Abrevia o dinheiro usando comparacoes, int, str e contas simples. 1k 1M 1B"""
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
    """Organiza os vinte niveis; carrega e dimensiona cada imagem uma vez."""
    info = {}
    for n in range(1, NIVEL_MAXIMO + 1):
        nome, arquivo, escala = BASE[n - 1]
        imagem = pygame.image.load(path.join(IMG_DIR, arquivo)).convert()
        # EXTRA AUTORIZADO: remove o preto do JPEG antes de redimensionar, usamos auxilio da IA 
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
