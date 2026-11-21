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

def escolher_direcao(self):  # Sorteia se o dinossauro fica parado ou anda em uma nova direcao.
        if random.randint(1, 10) <= 3:
            self.vx, self.vy = 0, 0
        else:
            self.vx = random.randint(-43, 43) / 1000
            self.vy = random.randint(-19, 19) / 1000
        self.tempo_direcao = random.randint(1000, 3000)

def update(self, dt):  # Atualiza o contador de ovos e move o dino dentro dos limites do gramado. rect=tela do jogo
        self.tempo_ovo -= dt
        if not self.preso:
            self.tempo_direcao -= dt
            if self.tempo_direcao <= 0:
                self.escolher_direcao()
            self.x += self.vx * dt
            self.y += self.vy * dt
            self.rect.x = int(self.x)
            self.rect.y = int(self.y)
            if self.rect.left < X_MIN:
                self.rect.left = X_MIN
                self.x = self.rect.x
                self.vx = -self.vx
            if self.rect.right > X_MAX:
                self.rect.right = X_MAX
                self.x = self.rect.x
                self.vx = -self.vx
            if self.rect.top < Y_MIN:
                self.rect.top = Y_MIN
                self.y = self.rect.y
                self.vy = -self.vy
            if self.rect.bottom > Y_MAX:
                self.rect.bottom = Y_MAX
                self.y = self.rect.y
                self.vy = -self.vy
class Ovo(pygame.sprite.Sprite):
#Um ovo coletavel, com valor ligado ao nivel e vida de doze segundos.

    def __init__(self, x, y, nivel, assets):  # Cria um ovo na posicao (x, y) com valor proporcional ao nivel.
        pygame.sprite.Sprite.__init__(self)
        self.image = assets["ovo"].render("O", True, (255, 240, 194))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.valor = valor_ovo(nivel)
        self.vida = VIDA_OVO * 1000

    def update(self, dt):  # Desconta o tempo de vida do ovo e remove-o se passar de 12 segundos.
        self.vida -= dt
        if self.vida <= 0:
            self.kill()


class Caixa(pygame.sprite.Sprite):
#Uma entrega que cai no campo e depois se transforma em um dinossauro.

    def __init__(self, nivel, x, y, assets):  
# Cria uma caixa acima da tela que vai cair ate o ponto (x, y).
        pygame.sprite.Sprite.__init__(self)
        self.image = assets["grande"].render("?", True, (255, 225, 144))
        self.rect = self.image.get_rect()
        self.rect.center = (x, -30)
        self.y = -30
        self.y_alvo = y
        self.nivel = nivel
        self.espera = 700
        self.estado = "caindo"

    def update(self, dt):  # Anima a queda da caixa ate o chao e conta 0,7s antes de abrir.
        if self.estado == "caindo":
            self.y += 0.45 * dt
            if self.y >= self.y_alvo:
                self.y = self.y_alvo
                self.estado = "parada"
            self.rect.centery = int(self.y)
        else:
            self.espera -= dt

   


    

