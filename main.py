#Trabalho Final - Batalha Naval
#Arquivo da Função Main
#
#Grupo composto por: 
#
# Douglas Salustrino de Oliveira
# Pedro Kauã dos Santos do Prado
# Rafael Martins Ferreira


#Importando as funções do arquivo auxiliar.py
from auxiliar import imprimir_mapa, criar_mapa, gerar_navio, jogada, alterar_mapa, alterar_mapa2, jog1_ganhou, jog2_ganhou

#Função main que roda o jogo Batalha Naval, sendo chamado as funções que printam o mapa, navios e sua quantidade.
def main():
    regras = input("Digite R para ver as regras ou então aperte qualquer outra tecla para começar: ")
    if regras == "R":
        print("Batalha naval é um jogo de tabuleiro de dois jogadores, no qual os jogadores têm de adivinhar em que quadrados estão os navios do oponente;\n\n"
        "* O jogador1 começa atacando alguma cordenada dada por uma letra entre A e J e logo em seguida um numero de 0 a 9;\n"
        "* Se o jogador1 acertar ele jogará de novo, se não a vez é passada ao jogador2;\n"
        "* O jogo acaba quando o primeiro jogador afundar todas as embarcações;\n" 
        "* Use o comando: 'sair' se deseja sair da partida;\n"
        "* Use o comando: reiniciar se deseja 'reiniciar' a partida;\n"
        "* Use o comando embarcacoes se deseja ver quantas embarcações foram afundadas.\n\n")

    input("Digite qualquer tecla para continuar...")

    mapa = criar_mapa(10)
    mapa2 = criar_mapa(10)
    imprimir_mapa(mapa, mapa2)
    porta = gerar_navio(5, mapa)
    tanque = gerar_navio(4, mapa)
    tanque2 = gerar_navio(4, mapa)
    contra = gerar_navio(3, mapa)
    contra2= gerar_navio(3, mapa)
    contra3 = gerar_navio(3, mapa)
    sub = gerar_navio(2, mapa)
    sub2 = gerar_navio(2, mapa)
    sub3 = gerar_navio(2, mapa)
    sub4 = gerar_navio(2, mapa)
    porta_2 = gerar_navio(5, mapa)
    tanque_2 = gerar_navio(4, mapa)
    tanque2_2 = gerar_navio(4, mapa)
    contra_2 = gerar_navio(3, mapa)
    contra2_2 = gerar_navio(3, mapa)
    contra3_2 = gerar_navio(3, mapa)
    sub_2 = gerar_navio(2, mapa)
    sub2_2 = gerar_navio(2, mapa)
    sub3_2 = gerar_navio(2, mapa)
    sub4_2 = gerar_navio(2, mapa)
    navios = [porta, tanque, tanque2, contra, contra2, contra3, sub, sub2, sub3, sub4]
    navios2 = [porta_2, tanque_2, tanque2_2, contra_2, contra2_2, contra3_2, sub_2, sub2_2, sub3_2, sub4_2]
    tentativas = []
    tentativas2 = []
    quant_navio1 = 10
    quant_navio2 = 10
#Determina qual dos jogadores venceu a partida
    while quant_navio1 != 0 or quant_navio2 != 0:
        acertou = True
        while acertou == True:
            for i in navios:
                cont = 0
                for j in i:
                    if j in tentativas:
                        cont += 1
                if cont == len(i):
                    quant_navio1 -= 1
                    navios.remove(i)
                if quant_navio1 == 0:
                    return jog2_ganhou    
            resultado = alterar_mapa(jogada(), mapa, navios, tentativas)
            print('Vez do jogador 1')
            mapa = resultado[0]
            acertou = resultado[1]
            imprimir_mapa(mapa, mapa2)
            print(navios)
            print(navios2)
            print('Quantidade de navios do jogador 1: {}'.format(quant_navio2))
            print('Quantidade de navios do jogador 2: {}'.format(quant_navio1))
            if acertou == False:
                acertou2 = True
            while acertou2 == True:
                for i in navios2:
                    cont = 0
                    for j in i:
                        if j in tentativas2:
                            cont += 1
                    if cont == len(i):
                        quant_navio2 -= 1
                        navios2.remove(i)
                    if quant_navio2 == 0:
                        return jog1_ganhou
                    if acertou2 == False:
                        acertou = True   
                resultado2 = alterar_mapa2(jogada(), mapa2, navios2, tentativas2)
                print('Vez do jogador 2')
                mapa2 = resultado2[0]
                acertou2 = resultado2[1]
                imprimir_mapa(mapa, mapa2)
                print('Quantidade de navios do jogador 1: {}'.format(quant_navio2))
                print('Quantidade de navios do jogador 2: {}'.format(quant_navio1))
        if acertou2 == False:
            acertou = True

if __name__ == "__main__":
    main()