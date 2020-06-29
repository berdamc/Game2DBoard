from game2dboard import *
from random import randint     # gerar números aleatórios
import pygame                  # somente para sons


pontos = 0
total = 0
linha = 0
coluna = 0
valorTimer = 1000
trocaColuna = False
trocaLinha = False

pygame.init()                                #inicializa pygame a configura os sons
perdeu = pygame.mixer.Sound("perdeu.wav")
ponto = pygame.mixer.Sound("ponto.wav")


def updateTela():                #imprime na base da tela os pontos e a qtde de movimentações da bola
    b.print(pontos, "/", total)


def mouse_fn(button, row, col):                 #executa essa função nos cliques do mouse nas células do jogo
    global pontos,linha,trocaColuna,valorTimer  #variáveis globais
    if b[row][col] == "bola.png":               #se na célula existir uma bola
        pontos += 1                             #soma os pontos
        updateTela()                          #atualiza os pontos na tela
        pygame.mixer.Sound.play(ponto)          #toca o som de pontuação

        valorTimer = valorTimer - 50            #diminui o intervalo que a bola troca de célula, cada clique certo, o tempo diminui
        if valorTimer >= 50:
            b.start_timer(valorTimer)

        trocaColuna = True                      #deve-se alterar a coluna aleatoriamente
        linha = 0                               #inicia na linha 0, linha superior
    else:
        b.on_mouse_click = 0                    # quando o jogador n acerta a bola, o jogo é terminado
        b.on_timer = 0
        pygame.mixer.Sound.play(perdeu)         # toca o som de perda

def timer_fn():                                          #funcao que executa a cada segundo
    global pontos, coluna, total, linha,trocaColuna

    b.clear()                                            #limpa a tela

    if trocaColuna == True:                              #quando o jogador acerta o movimento anterior
        coluna = randint(0, 9)                           # a bola inicia em uma nova coluna na linha 0
        trocaColuna = False                              # observe linha 34,35

    b[linha][coluna] = "bola.png"                        #depois de limpada a tela na linha 44, a figura da bola é adicionada
    linha = linha + 1                                    # a bola é inserida na linha + 1

    if linha == 10:                                      # se a bola chegar na linha 10 que é o final do quadro
       linha = 0                                         # a bola inicia na linha 0 e nova coluna
       trocaColuna = True

    total += 1                                           #incrementa a qtde de jogadas e atualiza tela
    updateTela()


b = Board(10, 10)                                        #cria a tela
b.title = "Take the ball"                                #Título da tela
b.cursor = "draped_box"                                  # tipo do cursos
b.cell_size = (50, 50)                                   #tamanho da célula
b.cell_color = "blue"                                    #cor da célula
b.cell_spacing = 1
b.grid_color = b.margin_color = "white"
b.create_output(background_color="gray10", color="white")
b.on_mouse_click = mouse_fn                                 #define a função mouse_fn que é executada no click
b.on_timer = timer_fn                                       # a cada tanto tempo executa a função timer_fn
b.start_timer(valorTimer)                                   #define o tempo de 1000 milisegundos para ser executada a função de timer
b.show()                                                    #mostra a tela