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
                    # =====LEITURA E VALIDAÇÃO DA JOGADA 
                    # O while repete a leitura até a jogada ser válida.
                    acao_valida = False
                    while not acao_valida:
                        acao = input(f"{jogador} ({marca}), escolha a casa (ex.: B2): ")

                        # for aninhado que procura a jogada digitada entre as 9 casas:
                        # o for de fora (i) percorre as linhas e define a letra (A, B ou C);
                        # o for de dentro (j) percorre as colunas e monta o texto da casa,
                        # por exemplo "B" + "2" = "B2". Se a entrada for igual ao texto
                        # de alguma casa, guardamos a linha e a coluna dela.
                        linha = -1         # -1 significa "ainda não achou a casa"
                        coluna = -1
                        for i in range(3):
                            if i == 0:
                                maiuscula = "A"
                                minuscula = "a"
                            elif i == 1:
                                maiuscula = "B"
                                minuscula = "b"
                            else:
                                maiuscula = "C"
                                minuscula = "c"
                            for j in range(3):
                                if acao == maiuscula + str(j + 1) or acao == minuscula + str(j + 1):
                                    linha = i
                                    coluna = j

                        if acao == "":
                            print("Você não digitou nada. Digite uma letra (A a C) e um número (1 a 3).")
                        elif linha == -1:
                            print("Jogada inválida. Digite a linha (A a C) e a coluna (1 a 3), ex.: B2.")
                        elif tabuleiro[linha][coluna] != " ":
                            print("Essa casa já está ocupada. Escolha outra.")
                        else:
                            acao_valida = True
                # =====  MARCA A AÇÃO  =====
                    tabuleiro[linha][coluna] = marca
                    rodada = rodada + 1
                    
                 # ===== VENCENDO =====
                    for i in range(3):
                        # linha i completa com o símbolo do jogador atual
                        if tabuleiro[i][0] == marca and tabuleiro[i][1] == marca and tabuleiro[i][2] == marca:
                            venceu = True
                        # coluna i completa com o símbolo do jogador atual
                        if tabuleiro[0][i] == marca and tabuleiro[1][i] == marca and tabuleiro[2][i] == marca:
                            venceu = True
                    # diagonal principal (A1, B2, C3)
                    if tabuleiro[0][0] == marca and tabuleiro[1][1] == marca and tabuleiro[2][2] == marca:
                        venceu = True
                    # diagonal secundária (A3, B2, C1)
                    if tabuleiro[0][2] == marca and tabuleiro[1][1] == marca and tabuleiro[2][0] == marca:
                        venceu = True
