import forca
import adivinhacao

def escolher():
    print('*************************')
    print('*****escolha o jogo!*****')
    print('*************************')

    jogo = int(input("(1) forca  (2) adivinhação - "))

    if jogo == 1:
        print('jogando o jogo 1')
        forca.jogar()
    elif jogo ==2:
        print('jogando o jogo 2')
        adivinhacao.jogar()
if __name__ == "__main__":
    escolher()