import pygame 
import random
from config import *
from assets import *
import math
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
        # Controle da animacao
        self.tempo_animacao = random.uniform(0, 6.28)
        self.andando = False
        self.angulo_animacao = 0
        self.salto_animacao = 0
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
        # Detecta se o dinossauro esta andando
        self.andando = (
            not self.preso
            and (self.vx != 0 or self.vy != 0)
        )

        if self.andando:
            self.tempo_animacao += dt * 0.012

            # Balanco do corpo
            self.angulo_animacao = (
                math.sin(self.tempo_animacao) * 3
            )

            # Pequena subida e descida
            self.salto_animacao = (
                abs(math.sin(self.tempo_animacao)) * 3
            )
        else:
            self.angulo_animacao = 0
            self.salto_animacao = 0

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
class Partida:
    #Guarda moedas, sprites, compras, melhorias, sorteio e condicao de vitoria.

    def __init__(self, assets):  # Inicia uma partida nova com 100 moedas e dois dinos nivel 1.
        self.assets = assets
        self.moedas = 100
        self.dinos = pygame.sprite.Group()
        self.ovos = pygame.sprite.Group()
        self.caixas = pygame.sprite.Group()
        self.compradas = [0] * NIVEL_MAXIMO
        self.ent_lvl = 0
        self.qual = 1
        self.maior = 1
        self.timer = 3000
        self.tempo = 0
        self.aviso = "Junte dois dinos iguais para evoluir!"
        self.aviso_t = 4000
        self.venceu = False
        self.girando = False
        self.tempo_giro = 0
        self.proxima_troca = 0
        self.roleta_cd = 0
        self.cursor_roleta = 0
        self.premio = 0
        self.resultado = ""
        self.aparecer_dino(1, 260, 340)
        self.aparecer_dino(1, 510, 390)

    def avisar(self, mensagem):  # Mostra uma mensagem rapida na tela por 2,8 segundos.
        self.aviso = mensagem
        self.aviso_t = 2800

    def ocupados(self):  # Retorna a soma de dinossauros vivos e caixas fechadas no campo.
        return len(self.dinos) + len(self.caixas)

    def tem_espaco(self): # verifica se ainda cabe mais um dino ou uma caixa fechadas no campo
        return self.ocupados() < MAX_DINOS
    
    def renda(self): # calcula a medida de moedas geradas por seg. pelos dinos atuais
        total = 0
        for dino in self.dinos:
            total += valor_ovo(dino.nivel)
        return total / MEDIA_OVO
    def intervalo(self):  # Retorna o intervalo atual (em segundos) entre entregas automaticas.
        segundos = ENTREGA_BASE - ENTREGA_PASSO * self.ent_lvl
        if segundos < ENTREGA_MIN:
            segundos = ENTREGA_MIN
        return segundos

    def limite_compra(self):  # Calcula o nivel maximo desbloqueado para compra na loja.
        limite = self.maior - 1
        if limite < 4:
            limite = 4
        if limite >= NIVEL_MAXIMO:
            limite = NIVEL_MAXIMO - 1
        return limite

    def custo_entrega(self):  # Retorna o preco da proxima melhoria de velocidade de entrega.
        return int(120 * 3 ** self.ent_lvl)
    def custo_qual(self):  # Retorna o preco da proxima melhoria de qualidade das caixas.
        return int(60 * 2.5 ** self.qual)

    def aparecer_dino(self, nivel, x, y):  # Cria um dinossauro no campo e atualiza o maior nivel alcancado.
        dino = Dino(nivel, x, y, self.assets)
        self.dinos.add(dino)
        if nivel > self.maior:
            self.maior = nivel
        return dino

    def posicao(self):  # Sorteia uma coordenada (x, y) valida dentro do gramado.
        x = random.randint(X_MIN + 65, X_MAX - 65)
        y = random.randint(Y_MIN + 45, Y_MAX - 45)
        return x, y
    
