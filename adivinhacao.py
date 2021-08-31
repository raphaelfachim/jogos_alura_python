import random as r

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = r.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Níveis: (1) Fácil (2) Médio (3) Difícil", numero_secreto)

    while (True):
        nivel = int(input("Escolha um nível: "))
        if nivel == 1:
            tentativas = 10
            break
        elif nivel == 2:
            tentativas = 5
            break
        elif nivel == 3:
            tentativas = 2
            break
        else:
            print("Digite um nível válido")
            continue

    for rodadas in range(1,tentativas+1):
        print("Rodada {} de {}".format(rodadas,tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        if(chute < 1 or chute > 100):
            print("O número deve estar entre 1 e 100!")
            continue
        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        if (acertou):
            print("Você acertou!\nPontuação: {}".format(pontos))
            break
        else:
            pontos_perdidos = abs(chute-numero_secreto)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("Seu chute foi maior que o número secreto")
                if (rodadas == tentativas):
                    print("Pontuação: 0")
            else:
                print("Seu chute foi menor que o número secreto")
                if (rodadas == tentativas):
                    print("Pontuação: 0")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
