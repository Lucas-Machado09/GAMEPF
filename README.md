
# Dino Evolution

Dino Evolution é um jogo 2D de evolução e fusão de dinossauros, desenvolvido em Python com a biblioteca Pygame.

O jogador combina dinossauros do mesmo nível, coleta ovos para ganhar moedas e investe em novos dinossauros e melhorias. O objetivo é alcançar os 20 níveis de evolução e criar o Rei T-Rex.

## Integrantes do grupo

- Lucas Andrade Machado
- Guilherme Tardelli Prieto
- Pedro Rinaldi

## Vídeo de demonstração

Link do vídeo: https://youtu.be/8nCeBJQJbW4

## Como jogar

Toda a interação é feita com o mouse. Na tela inicial, clique em **JOGAR** para começar ou em **Como jogar** para consultar as instruções.

A partida começa com **100 moedas e dois dinossauros de nível 1**.

- **Evoluir dinossauros:** clique, segure e arraste um dinossauro sobre outro do mesmo nível. Ao soltar, os dois se transformam em um dinossauro do nível seguinte.
- **Coletar moedas:** clique nos ovos que aparecem no campo antes que desapareçam. O valor de cada ovo depende do nível do dinossauro que o produziu.
- **Comprar dinossauros:** abra o painel **Dinos** e utilize moedas para comprar os níveis disponíveis. Use a roda do mouse ou os botões de navegação para percorrer a loja.
- **Comprar melhorias:** abra o painel **Melhorias** para reduzir o intervalo entre as entregas automáticas e aumentar o nível dos dinossauros que chegam nas caixas.
- **Girar a roleta:** abra o painel **Roleta** e clique em **GIRAR** para receber moedas ou uma caixa especial. Após cada giro, há uma espera de **1 minutos**.
- **Vencer:** combine dois dinossauros de nível 19 para criar o **Rei T-Rex, de nível 20**, e concluir a partida.

## Regras importantes

- O campo comporta até **20 dinossauros e caixas somados**.
- Os ovos desaparecem após **6 segundos**.
- A loja começa com os níveis 1 a 4 disponíveis. Novas compras são liberadas conforme a evolução dos dinossauros.
- O dinossauro de nível 20 só pode ser obtido por fusão.
- Os painéis de Dinos, Melhorias e Roleta pausam os acontecimentos do campo. A animação e o tempo de espera da roleta continuam sendo atualizados.

## Requisitos

- Python 3.13.
- Pygame 2.6.1.
- Os arquivos do projeto e as pastas `imagens/` e `sons/` completos.

Os módulos `random`, `math` e `os` fazem parte do Python e não precisam ser instalados separadamente.

## Instalação e execução

Baixe ou clone o repositório e abra um terminal na pasta que contém os arquivos `funcoes.py`, `assets.py` e `config.py`.

### Windows

Com o Python 3.13 instalado, execute os comandos abaixo, um por vez:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install pygame==2.6.1
.\.venv\Scripts\python.exe funcoes.py
```

Nas próximas vezes, abra o terminal na pasta do projeto e execute apenas:

```powershell
.\.venv\Scripts\python.exe funcoes.py
```

### Linux ou macOS

Com o Python 3.13 instalado, execute:

```bash
python3.13 -m venv .venv
./.venv/bin/python -m pip install pygame==2.6.1
./.venv/bin/python funcoes.py
```

Nas próximas vezes, execute apenas:

```bash
./.venv/bin/python funcoes.py
```

### Execução pelo VS Code

1. Abra a pasta do projeto no VS Code.
2. Pressione `Ctrl + Shift + P`.
3. Procure por `Python: Select Interpreter`.
4. Selecione o Python da pasta `.venv`.
5. Abra o arquivo `funcoes.py` e clique em **Run Python File**.

## Estrutura do projeto

```text
DinoEvolution/
├── funcoes.py
├── assets.py
├── config.py
├── imagens/
├── sons/
└── README.md
```

- **`funcoes.py`:** contém as classes dos dinossauros, ovos e caixas, as regras da partida, os eventos do mouse, as telas e o loop principal.
- **`assets.py`:** carrega e redimensiona imagens, configura fontes e sons e fornece funções para desenhar os elementos da interface.
- **`config.py`:** reúne as configurações do jogo, como tamanho da janela, cores, níveis dos dinossauros, tempos, limites e probabilidades da roleta.
- **`imagens/`:** contém o cenário, o meteoro e as imagens dos 20 níveis de dinossauros.
- **`sons/`:** contém a trilha sonora e o efeito sonoro utilizado nas ações do jogo.

Mantenha os nomes dos arquivos e a organização das pastas, pois o jogo utiliza essa estrutura para localizar as imagens e os sons.

