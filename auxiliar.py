import random

def criar_mapa(tamanho):
    return [["~" for i in range(tamanho)] for i in range(tamanho)]

def imprimir_mapa(mapa, mapa2):
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

def gerar_navio(tamanho, mapa):
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

def jogada():
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

def alterar_mapa(tentativa, mapa, navio, tentativas):
    if tentativa in tentativas:
        print('Você já bonbardeou essa posição!!!')
        return mapa
    tentativas.append(tentativa)
    for i in navio:
        if tentativa in i:
            print('Você acertou um Navio!!!')
            mapa[tentativa[0]][tentativa[1]] = 'X'
            return mapa
    mapa[tentativa[0]][tentativa[1]] = "*"
    return mapa

def alterar_mapa2(tentativa2, mapa2, navio2, tentativas2):
    if tentativa2 in tentativas2:
        print('Você já bonbardeou essa posição!!!')
        return mapa2
    tentativas2.append(tentativa2)
    for i in navio2:
        if tentativa2 in i:
            print('Você acertou um Navio!!!')
            mapa2[tentativa2[0]][tentativa2[1]] = 'X'
            return mapa2
    mapa2[tentativa2[0]][tentativa2[1]] = "*"
    return mapa2





