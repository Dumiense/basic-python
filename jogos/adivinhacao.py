def jogar():

    import random
    num_secreto = round(random.randrange(1, 101))
    tentativa = 0
    pontos = 1000
    perdidos = 0

    print('selecione o nível de dificuldade')
    print('(1) fácil (2) médio (3) dificil')
    nivel = int(input('nível: '))

    if nivel == 1:
        tentativa = 20
    elif nivel == 2:
        tentativa = 10
    elif nivel ==3:
        tentativa = 5

    for rodada in range(1, tentativa + 1):
        chute = int(input('digite um número entre 1 e 100: '))
        print(f'tentativa {rodada} de {tentativa}')

        if chute < 1 or chute > 100:
            print('o número deve ser entre 1 e 100!')
            continue

        if chute == num_secreto:
            print(f'você acertou! pontos: {pontos}')
            break
        else:
            if chute > num_secreto:
                print('você errou, o número é menor')
            if chute < num_secreto:
                print('você errou, o número é maior')
            perdidos = abs(num_secreto - chute)
            pontos = pontos - perdidos

        print('--------------------------------------------')
    print(f'o número secreto era {num_secreto}')

if __name__ == "__main__":
    jogar()
