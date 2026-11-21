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
    def nova_caixa(self, nivel):  # Faz cair uma nova caixa no campo se houver vaga disponivel.
            if not self.tem_espaco():
                return False
            x, y = self.posicao()
            self.caixas.add(Caixa(nivel, x, y, self.assets))
            return True
    
    def comprar_dino(self, nivel):  # Confere desbloqueio, espaco e moedas antes de comprar um dino.
        if nivel < 1 or nivel >= NIVEL_MAXIMO:
            self.avisar("O nivel 20 so pode ser criado por fusao.")
            return False
        if nivel > self.limite_compra():
            self.avisar("Alcance o nivel " + str(nivel + 1) + " para liberar.")
            return False
        if not self.tem_espaco():
            self.avisar("Campo cheio! Junte dois dinossauros.")
            return False
        custo = preco_dino(nivel, self.compradas)
        if self.moedas < custo:
            self.avisar("Faltam moedas para essa compra.")
            return False
        self.moedas -= custo
        compra_dino(nivel, self.compradas)
        x, y = self.posicao()
        self.aparecer_dino(nivel, x, y)
        self.assets["comprar"].play()
        self.avisar("Dinossauro nivel " + str(nivel) + " comprado!")
        return True
    def comprar_melhoria(self, tipo):  # Aplica uma melhoria de entrega ou qualidade das caixas.
        if tipo == "entrega":
            if self.ent_lvl >= ENT_MAX:
                self.avisar("Entrega ja esta no nivel maximo.")
                return False
            custo = self.custo_entrega()
        else:
            if self.qual >= QUAL_MAX:
                self.avisar("Qualidade ja esta no nivel maximo.")
                return False
            custo = self.custo_qual()
        if self.moedas < custo:
            self.avisar("Faltam moedas para essa melhoria.")
            return False
        self.moedas -= custo
        if tipo == "entrega":
            self.ent_lvl += 1
            if self.timer > self.intervalo() * 1000:
                self.timer = self.intervalo() * 1000
        else:
            self.qual += 1
        self.assets["comprar"].play()
        self.avisar("Melhoria comprada!")
        return True

    def mesclar(self, primeiro, segundo):  # Funde dois dinos iguais em um de nivel superior e verifica vitoria.
        if primeiro == segundo or primeiro not in self.dinos or segundo not in self.dinos:
            return False
        if primeiro.nivel != segundo.nivel:
            self.avisar("Escolha dois dinossauros do mesmo nivel.")
            return False
        if primeiro.nivel >= NIVEL_MAXIMO:
            return False
        nivel = primeiro.nivel + 1
        x, y = segundo.rect.center
        primeiro.kill()
        segundo.kill()
        self.aparecer_dino(nivel, x, y)
        self.assets["encaixe"].play()
        self.avisar("Nova evolucao: " + self.assets["dinos"][nivel]["nome"] + "!")
        if nivel == NIVEL_MAXIMO:
            self.venceu = True
            self.assets["vitoria"].play()
        return True
    def coletar_ovo(self, ovo):  # Adiciona o valor do ovo as moedas e remove o ovo da tela.
        if ovo not in self.ovos:
            return False
        self.moedas += ovo.valor
        self.avisar("+" + dinheiro(ovo.valor) + " moedas")
        ovo.kill()
        self.assets["coletar"].play()
        return True

    def sortear_premio(self):  # Sorteia um premio da roleta respeitando os pesos definidos em config.py.
        total = 0
        for peso in PESOS:
            total += peso
        sorteio = random.randint(1, total)
        acumulado = 0
        for i in range(len(PESOS)):
            acumulado += PESOS[i]
            if sorteio <= acumulado:
                return i

    def girar(self):  # Inicia a animacao de giro da roleta se nao estiver em recarga.
        if self.girando or self.roleta_cd > 0:
            self.avisar("A roleta ainda esta em espera.")
            return False
        self.premio = self.sortear_premio()
        self.girando = True
        self.tempo_giro = 0
        self.proxima_troca = 0
        self.resultado = ""
        return True
    
    def dar_premio(self):  # Entrega moedas ou uma caixa ao finalizar o giro da roleta.
        tipo, valor = PREMIOS[self.premio]
        if tipo == "renda":
            ganho = int(self.renda() * valor)
            if ganho < 25:
                ganho = 25
            self.moedas += ganho
            self.resultado = "+" + dinheiro(ganho) + " moedas!"
        else:
            nivel = self.qual + valor
            if nivel >= NIVEL_MAXIMO:
                nivel = NIVEL_MAXIMO - 1
            if self.nova_caixa(nivel):
                self.resultado = "Caixa com dino nivel " + str(nivel) + "!"
            else:
                ganho = preco_dino(nivel, self.compradas)
                self.moedas += ganho
                self.resultado = "Campo cheio: +" + dinheiro(ganho) + " moedas!"
        self.assets["coletar"].play()

    def atualizar_roleta(self, dt):  # Atualiza os 4 segundos de animacao do giro e o cooldown.
        if self.girando:
            self.tempo_giro += dt
            if self.tempo_giro >= self.proxima_troca:
                self.cursor_roleta += 1
                if self.cursor_roleta >= len(PREMIOS):
                    self.cursor_roleta = 0
                self.proxima_troca = self.tempo_giro + 70 + int(280 * (self.tempo_giro / 4000) ** 2)
            if self.tempo_giro >= 4000:
                self.girando = False
                self.cursor_roleta = self.premio
                self.roleta_cd = COOLDOWN_ROLETA * 1000
                self.dar_premio()
        elif self.roleta_cd > 0:
            self.roleta_cd -= dt
            if self.roleta_cd < 0:
                self.roleta_cd = 0
    def update(self, dt, mundo_ativo):  # Atualiza dinos, ovos, caixas e entregas quando nenhum painel esta aberto.
        self.atualizar_roleta(dt)
        if self.aviso_t > 0:
            self.aviso_t -= dt
        if mundo_ativo:
            self.tempo += dt
            for dino in self.dinos:
                dino.update(dt)
            for ovo in objetos_do_grupo(self.ovos):
                ovo.update(dt)
            for caixa in self.caixas:
                caixa.update(dt)
            for dino in self.dinos:
                if dino.tempo_ovo <= 0:
                    dino.tempo_ovo = random.randint(OVO_MIN, OVO_MAX) * 1000
                    if len(self.ovos) < MAX_OVOS:
                        x = dino.rect.centerx + random.randint(-14, 14)
                        y = dino.rect.bottom + 6
                        self.ovos.add(Ovo(x, y, dino.nivel, self.assets))
            for caixa in objetos_do_grupo(self.caixas):
                if caixa.estado == "parada" and caixa.espera <= 0:
                    x, y = caixa.rect.center
                    nivel = caixa.nivel
                    caixa.kill()
                    self.aparecer_dino(nivel, x, y)
            if self.tem_espaco():
                self.timer -= dt
                if self.timer <= 0:
                    self.nova_caixa(self.qual)
                    self.timer = self.intervalo() * 1000
    
# ==================== CONTROLE DE TELAS E MOUSE ====================
class InterfaceMouse:
    #Gerencia telas, cliques, arrasto de dinossauros e animacao do meteoro.
        def _init_(self, assets):  # Inicializa estados de tela, variaveis de arrasto e do meteoro.
            self.assets = assets
            self.partida = Partida(assets)
            self.estado = "menu"
            self.voltar_ajuda = "menu"
            self.painel = ""
            self.scroll = 0
            self.mouse = (0, 0)
            self.arrastado = 0
            self.offset = (0, 0)
            self.efeitos = []
            self.confetes = []
            self.passo_roda = 0
            self.inicio_roda = 0
            self.total_roda = 0
            self.meteoro_x = 0
            self.meteoro_y = 0
            self.tempo_meteoro = 0
            self.menu_dinos = []
            for nivel in [1, 3, 5, 8, 12, 17]:
                x = random.randint(90, WIDTH - 90)
                y = random.randint(360, 490)
                self.menu_dinos.append(Dino(nivel, x, y, assets))

        def botao(self, tela, area, titulo, cor=(76, 155, 76), ativo=True, fonte="fonte"):  # Desenha um botao clicavel com efeito hover.
            if not ativo:
                cor = (142, 137, 115)
            elif dentro(self.mouse, area):
                nova_cor = []
                for canal in cor:
                    canal += 20
                    if canal > 255:
                        canal = 255
                    nova_cor.append(canal)
                cor = nova_cor
            placa(tela, area, cor)
            x, y, largura, altura = area
            escrever(tela, self.assets, titulo, x + largura / 2, y + altura / 2 - 1, fonte, centro=True)

        def iniciar(self):  # Comeca uma nova partida zerando os estados anteriores.
            self.partida = Partida(self.assets)
            self.estado = "jogo"
            self.painel = ""
            self.scroll = 0
            self.arrastado = 0
            self.efeitos = []
            self.confetes = []
            self.passo_roda = 0
            self.tempo_meteoro = 0

        def area_compra(self, linha):  # Calcula a area clicavel do botao Comprar de uma linha da loja.
            return (569, 149 + linha * 57, 128, 34)

        def mudar_scroll(self, passo):  # Move a rolagem da loja entre os 20 niveis disponiveis.
            self.scroll += passo
            if self.scroll < 0:
                self.scroll = 0
            if self.scroll > NIVEL_MAXIMO - 6:
                self.scroll = NIVEL_MAXIMO - 6

        def alvo(self, dino):  # Encontra um dinossauro do mesmo nivel proximo ao que esta sendo arrastado.
            melhor = 0
            menor = 999999
            for outro in self.partida.dinos:
                if outro != dino and outro.nivel == dino.nivel and dino.nivel < NIVEL_MAXIMO:
                    distancia = calcular_distancia(dino.rect.centerx, dino.rect.centery,
                                                outro.rect.centerx, outro.rect.centery)
                    largura = dino.rect.right - dino.rect.left
                    outra_largura = outro.rect.right - outro.rect.left
                    alcance = int((largura + outra_largura) * 0.24) + 13
                    if distancia < alcance and distancia < menor:
                        melhor = outro
                        menor = distancia
            return melhor

