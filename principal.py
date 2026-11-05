# PRIMEIRO TÓPICO DA ATIVIDADE

# VARIÁVEIS

opcao = ""
jogador_1 = ""
jogador_2 = ""

# MENU INTERATIVO 

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


