import random
robo = random.randrange(0,5)
usuaria = int(input('Digite um numero de 1 a 5: '))
if robo == usuaria:
    print('Voce acertou o mesmo numero do robo!')
else:
    print('Voce não acerto o mesmo numero do robo!')
