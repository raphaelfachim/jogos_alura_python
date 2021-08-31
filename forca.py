import random

def mensagem_abertura():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")
    return 0

def ler_arquivo():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    rand = random.randrange(0, len(palavras))
    palavra_secreta = palavras[rand].upper()
    return palavra_secreta

def jogar():

    mensagem_abertura()

    palavra_secreta = ler_arquivo()

    acertou = False
    enforcou = False
    lista_acertos = list("_"*len(palavra_secreta))
    #lista_acertos = ["_" for letra in palavra_secreta]
    erros = 0

    print(lista_acertos)

    while(not acertou and not enforcou):
        chute = input("Digite uma letra: ").strip().upper()
        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    lista_acertos[index] = chute
                index += 1
        else:
            erros += 1
        acertou = "_" not in lista_acertos
        enforcou = (erros == 6)
        print(lista_acertos)
        if (acertou):
            print("Vitória")

        if (enforcou):
            print("Derrota, a palavra era {}".format(palavra_secreta))


    print("Fim de jogo")

if (__name__=="__main__"):
    jogar()