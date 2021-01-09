#Bibliotecas

import random

def jogar():
    print("---------------------------------")
    print("Bem vindo ao jogo de adivinhação!")
    print("---------------------------------")


    # Variáveis
    numero_secreto = random.randrange (1, 101)
    total_de_tentativas = 0
    pontos = 1000

    # Adicionando níveis ao jogo.

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    #Logica do programa
    for rodada in range(1, total_de_tentativas + 1): #  Enquanto a condição for verdadeira, irá rodar o bloco
        print("Tentativas {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str, end="\n")
        chute = int(chute_str) # convertendo o imput (chute_str) que é alocado como str para int atraves da variavel (chute) .


        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue


        # condições
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if (acertou):
            print("Você acertou e fez {} pontos!!".format(pontos), end="\n")
            break
        else:
            if (maior):
                print("Você errou! o seu chute foi maior que o número secreto" , end="\n")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif (menor):
                print("Você errou! o seu chute foi menor que o número secreto", end="\n")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
