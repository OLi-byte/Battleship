from auxiliar import imprimir_mapa, criar_mapa, gerar_navio, jogada, alterar_mapa, alterar_mapa2

def main():
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
    print(navios)
    print(navios2)
    tentativas = []
    tentativas2 = []
    while navios != [] or navios2 != []:
        for i in navios:
            if i == 0:
                navios.remove(i)
        quat_navios_jog1 = len(navios)
        print(quat_navios_jog1)
        mapa = alterar_mapa(jogada(), mapa, navios, tentativas)
        imprimir_mapa(mapa, mapa2)
        for j in navios2:
            if j == 0:
                navios2.remove(i)
        quat_navios_jog2 = len(navios2)
        print(quat_navios_jog2)   
        mapa2 = alterar_mapa2(jogada(), mapa2, navios2, tentativas2)
        imprimir_mapa(mapa, mapa2)
    print("Venceu")
    return

if __name__ == "__main__":
    main()
