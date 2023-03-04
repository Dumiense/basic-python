import random

def jogar():

    mensagem_abertura()
    palavra_secreta = carregar_palavra()
    acertos = verificar_acertos(palavra_secreta)
    print(acertos)

    erros = 0
    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = recebe_chute()

        if chute in palavra_secreta:
            marca_chute(chute, palavra_secreta, acertos)
        else:
            erros += 1
            desenha_forca(erros)
        print (acertos)
        enforcou = erros == 7
        acertou = "_" not in acertos
    if acertou:
        mensagem_vitoria()
    else:
        mensagem_derrota(palavra_secreta)

def mensagem_abertura():
    print("__________________________")
    print("bem vindo ao jogo da forca")
    print("__________________________")

def carregar_palavra():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    num = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num].upper()
    return palavra_secreta

def verificar_acertos(palavra):
    return ["_" for i in palavra]

def recebe_chute():
    chute = input('qual letra? ')
    chute = chute.strip().upper()
    return chute

def marca_chute(chute, palavra, acertos):
    index = 0
    for i in palavra:
        if chute == i:
            acertos[index] = i
        index += 1

def mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_derrota(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()