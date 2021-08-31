import adivinhacao
import forca
def escolher_jogo():
    print("Escolha um jogo:")
    codigo_jogo = int(input("(1) Adivinhação (2) Forca\n"))
    if(codigo_jogo == 1):
        adivinhacao.jogar()
    elif (codigo_jogo == 2):
        forca.jogar()
if (__name__ == "__main__"):
    escolher_jogo()