# PRIMEIRO TÓPICO DA ATIVIDADE

# VARIÁVEIS

opcao = ""
jogador_1 = ""
jogador_2 = ""

# MENU INTERATIVO 


tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
while opcao != "4":
    print("")
    print("============== MENU ==============")
    print("1 - Jogar")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")
    print("==================================")
    opcao = input("Escolha uma opção: ")

# ===== OPÇÃO DE JOGO DA VELHA =========
    if opcao == "1":
        print("")
        print("")
        print("==================================")
        print("          JOGO DA VELHA                 ")
        print("==================================")

        while jogador_1 == "":
            jogador_1 = input("Nome do jogador 1 (será o X): ")
            if jogador_1 == "":
                print("O nome não pode ficar vazio.")

        while jogador_2 == "" or jogador_2 == jogador_1:
            jogador_2 = input("Nome do jogador 2 (será o O): ")
            if jogador_2 == "":
                print("O nome não pode ficar vazio.")
            elif jogador_2 == jogador_1:
                print("Os dois jogadores precisam ter nomes diferentes.")

# ===== OPÇÃO DE REGRAS  =====
    elif opcao == "2":
        print("Regras")
    
# ===== OPÇÃO DE VER PLACAR  =====
    elif opcao == "3":
        print("Placar")
        
# ===== OPÇÃO DE SAIR E VER PLACAR =====
    elif opcao == "4":
        print("==========================")
        print("Até a próxima jogatina!")
        print("==========================")

        if opcao == "1":
         nova_partida = "S"

        # =====  OPCAAO: JOGAR NOVAMENTE =====
        # Este while repete a partida sem reiniciar o programa.
        while nova_partida == "S":
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = " "

            marca = "X"       # o X sempre começa
            fim = False       # vira True quando alguém vence ou dá empate
            venceu = False    # vira True se o jogador da vez completar uma linha, coluna ou diagonal
            rodada = 0        # conta as jogadas feitas nesta partida
            encerrar = False  # vira True depois de mostrar o tabuleiro final

            # ===== SEQUÊNCIA DA PARTIDA =====
            # Cada volta mostra o tabuleiro e, se a partida não acabou, faz uma jogada.
            # Na última volta (fim = True) só mostra o tabuleiro final e encerra o laço.
            while not encerrar:

             # ===== TABULEIRO NA TELA =====
                print("")
                if fim:
                    print("-------- Tabuleiro final --------")
                else:
                    print(f"------------ Rodada {rodada + 1} ------------")
                print("      1   2   3")
                print("    +---+---+---+")

                for i in range(3):
                    if i == 0:
                        letras = "A"
                    elif i == 1:
                        letras = "B"
                    else:
                        letras = "C"
                    desenho = f"  {letras} |"
                    for j in range(3):
                        desenho = f"{desenho} {tabuleiro[i][j]} |"
                    print(desenho)
                    print("    +---+---+---+")

                if fim:
                    encerrar = True
                else:
                    if marca == "X":
                        jogador = jogador_1
                    else:
                        jogador = jogador_2
