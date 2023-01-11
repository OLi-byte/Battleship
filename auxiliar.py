#Trabalho Final - Batalha Naval
#Arquivo de Funções auxiliares
#
#Grupo composto por: 
#
# Douglas Salustrino de Oliveira
# Pedro Kauã dos Santos do Prado
# Rafael Martins Ferreira

import random

def criar_mapa(tamanho):
    '''Função que cria o mapa'''
    return [["~" for i in range(tamanho)] for i in range(tamanho)]

#Imprimi dois mapas de tamanho 10x10
def imprimir_mapa(mapa, mapa2):
    '''Função que irá mostrar os dois tabuleiros aos jogadores na tela'''
    abecedario = "ABCDEFGHIJKLMNOPQRST"
    print("Jogador 1")
    for i in range(len(mapa2)):
        letra = abecedario[i]
        print(f"   {(letra)}", end=" ")
    print()
    for fila in range(len(mapa2)):
        print(f"{fila} {mapa2[fila]}")
    print("-"*52)
    abecedario = "ABCDEFGHIJKLMNOPQRST"
    print("Jogador 2")
    for i in range(len(mapa)):
        letra = abecedario[i]
        print(f"   {(letra)}", end=" ")
    print()
    for fila in range(len(mapa)):
        print(f"{fila} {mapa[fila]}")

#Gera navios aleatoriamente
def gerar_navio(tamanho, mapa):
    '''Função que vai gerar todos os barcos do jogo aleatoriamente'''
    tamanho_barco = tamanho
    sentido = random.randint(0, 1)
    if sentido == 0:
        lin_barco = [random.randint(0, len(mapa) - 1)] * tamanho_barco
        col = random.randint(0, len(mapa) - tamanho_barco)
        col_barco = list(range(col, col + tamanho_barco))
        coordenadas = list(zip(lin_barco, col_barco))
    else:
        col_barco = [random.randint(0, len(mapa) - 1)] * tamanho_barco
        lin = random.randint(0, len(mapa) - tamanho_barco)
        lin_barco = list(range(lin, lin + tamanho_barco))
        coordenadas = list(zip(lin_barco, col_barco))
    return list(coordenadas)

#Responsável pelas jogadas
def jogada():
    '''Recebe do jogador coordenadas ,dadas por uma letra maiúscula e um número, que determinam onde o jogador vai atacar'''
    print("Jogue no seguinte formato com letra MAIÚSCULA: A,1\nDigite 'sair' para sair do jogo\nDigite 'reiniciar' para reiniciar o jogo")
    coordenadas = input("Coordenadas: ")
    if coordenadas == "sair":
        exit()
    if coordenadas == "reiniciar":
        jogada()
    nadas = coordenadas.split(",")
    coluna = nadas[0]
    if coluna == "A":
        coluna = 1
    elif coluna == "B":
        coluna = 2
    elif coluna == "C":
        coluna = 3
    elif coluna == "D":
        coluna = 4
    elif coluna == "E":
        coluna = 5
    elif coluna == "F":
        coluna = 6
    elif coluna == "G":
        coluna = 7
    elif coluna == "H":
        coluna = 8
    elif coluna == "I":
        coluna = 9
    elif coluna == "J":
        coluna = 10
    linha = int(nadas[1])
    return(linha, coluna - 1)

#Altera o mapa do jogador 1
def alterar_mapa(tentativa, mapa, navio, tentativas):
    '''Determina se o jogador 2 acertou ou não a posição correta de uma embarcação'''
    acertou = False
    if tentativa in tentativas:
        print('Você já bonbardeou essa posição!!!')
        acertou = False
        return (mapa,acertou)
    tentativas.append(tentativa)
    for i in navio:
        if tentativa in i:
            print('Você acertou um Navio!!!')
            mapa[tentativa[0]][tentativa[1]] = 'X'
            acertou = True
            return (mapa,acertou)
    mapa[tentativa[0]][tentativa[1]] = "*"
    return (mapa,acertou)

#Altera o mapa do jogador 2
def alterar_mapa2(tentativa2, mapa2, navio2, tentativas2):
    '''Determina se o jogador 1 acertou ou não a posição correta de uma embarcação'''
    acertou2 = False
    if tentativa2 in tentativas2:
        print('Você já bonbardeou essa posição!!!')
        acertou2 = False
        return (mapa2,acertou2)
    tentativas2.append(tentativa2)
    for i in navio2:
        if tentativa2 in i:
            print('Você acertou um Navio!!!')
            mapa2[tentativa2[0]][tentativa2[1]] = 'X'
            acertou2 = True
            return (mapa2,acertou2)
    mapa2[tentativa2[0]][tentativa2[1]] = "*"
    return (mapa2,acertou2)

def jog1_ganhou():
    print('Jogador 1 ganhou')
def jog2_ganhou():
    print('Jogador 2 ganhou')