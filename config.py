from os import path 

# larg / altura
WIDTH = 800
HEIGHT = 600

# os dinos 
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
IMG_DIR = path.join(path.dirname(__file__), "imagens")

SND_DIR = path.join(path.dirname(__file__), "sons")

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

# retangulo do lugar onde os dinos vão andar
X_MIN = 12 
X_MAX = WIDTH - 12
Y_MIN = 310
Y_MAX = HEIGHT - 60

FUNDO = "fundo-floresta.jpeg"
MUSICA = "dinosaur_extinction_old_classical_music_by_kris_klavenes_ending_soundtrack_05.02.2021.mp3"
METEORO = "Meteoro.png"
SOM_ENCAIXE = "encaixe.wav"

# o que vamos usar na roleta 
PREMIOS = [("renda", 30), ("caixa", 0), ("renda", 60), ("caixa", 1), ("renda", 15), ("caixa", 0), ("renda", 120), ("caixa", 2)]
ROTULOS = ["+30s", "Caixa", "+60s", "Caixa +1", "+15s", "Caixa", "+2min", "Caixa +2"]
PESOS = [30, 20, 20, 8, 30, 20, 4, 2]

# cores usadas
BRANCO = (245, 244, 231)
ESCURO = (18, 29, 29)
PAINEL = (27, 45, 43)
VERDE = (92, 205, 145)
DOURADO = (255, 207, 93)
CINZA = (172, 192, 181)
VERMELHO = (255, 140, 121)

