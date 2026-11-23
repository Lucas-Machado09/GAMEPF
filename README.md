Título do projeto; 1 - Dino Evolution
Nomes dos membros do seu grupo; 2 - Lucas Andrade Machado, Guilherme Tardelli Prieto, Pedro Rinaldi 
Explicação de como rodar o jogo; 3 - É um jogo na qual tem que ir juntanto os dinos do mesmo nivel para  
Endereço de um vídeo curto apresentando o seu jogo (você pode colocar o vídeo onde preferir: YouTube, Vimeo, etc. mas o professor precisa ter acesso através do link). Esse vídeo (pode ser alguns poucos segundos) deve mostrar o seu projeto funcionando. - link_youtube: 
Recomendamos que vocês também incluam no README.md uma descrição do seu projeto, como instalar as dependências (se usar alguma biblioteca adicional, como o PyGame) e como executar o programa. Esses pontos não são obrigatórios, mas são recomendados em qualquer projeto.
# DinoEvolution

**DinoEvolution** é um jogo 2D de evolução e fusão (*merge game*) desenvolvido em Python com a biblioteca **Pygame**. O jogador gerencia um habitat pré-histórico onde dinossauros produzem ovos que geram moedas. Ao arrastar e combinar dois dinossauros do mesmo nível, eles evoluem para uma nova espécie — passando por 20 estágios evolutivos até desbloquear o **Rei T-Rex** e concluir o jogo.

---

## Integrantes do Grupo
* [Nome Completo do Integrante 1]
* [Nome Completo do Integrante 2]
* [Nome Completo do Integrante 3]

## Vídeo de Demonstração
* [Clique aqui para assistir ao vídeo do DinoEvolution funcionando](COLE_AQUI_O_LINK_DO_VIDEO)

---

## Como Jogar
Toda a interação do jogo é feita com o **mouse**:

* **Evoluir dinossauros:** Clique, segure e arraste um dinossauro sobre outro do mesmo nível para fundi-los em uma espécie superior.
* **Coletar moedas:** Clique nos ovos que aparecem pelo gramado antes que desapareçam (cada ovo vale moedas de acordo com o nível do dinossauro que o produziu).
* **Loja de Dinos:** Compre diretamente dinossauros de níveis já desbloqueados para acelerar suas fusões.
* **Melhorias:** Invista moedas para diminuir o tempo entre entregas automáticas de caixas e aumentar o nível inicial dos dinossauros que chegam nelas.
* **Roleta da Evolução:** Gire a roleta a cada 2 minutos para ganhar bônus de moedas baseados na sua renda por segundo ou caixas especiais gratuitas.
* **Objetivo final:** Combinar dois dinossauros de nível 19 (**Giganotossauro**) para criar o nível 20 (**Rei T-Rex**).

---

## Pré-requisitos e Instalação

1. Certifique-se de ter o **Python 3** instalado em seu computador.
2. Instale a biblioteca **Pygame** pelo terminal ou prompt de comando:

```bash
pip install pygame
```

*(Caso utilize Linux ou macOS e o comando acima não funcione, utilize `pip3 install pygame`.)*

---

## Como Rodar o Jogo

1. Baixe ou clone este repositório para o seu computador.
2. Mantenha todos os arquivos (`funcoes.py`, `config.py`, `assets.py`) e as pastas (`imagens/` e `sons/`) juntos no mesmo diretório.
3. Abra o terminal dentro da pasta principal do projeto e execute:

```bash
python funcoes.py
```

*(No Linux ou macOS, caso necessário, execute `python3 funcoes.py`.)*

---

## Estrutura do Projeto

* `funcoes.py`: Arquivo principal que inicializa o Pygame, executa o loop do jogo, gerencia as telas, eventos de mouse, regras da partida e sprites (`Dino`, `Ovo`, `Caixa`).
* `config.py`: Centraliza as constantes do jogo, dimensões da janela, limites do gramado, coordenadas dos botões, probabilidades da roleta e a tabela com os 20 níveis de dinossauros.
* `assets.py`: Responsável por carregar e redimensionar as imagens, configurar fontes e áudios e desenhar os elementos gráficos da interface.
* `imagens/`: Contém o cenário, o meteoro e os sprites dos 20 dinossauros.
* `sons/`: Contém a trilha sonora e os efeitos sonoros do jogo.