import random
robo = random.choice(['Pedra', 'Papel', 'Tesoura'])
print(f'{robo}')
jogador = str(input('Diga qual ira jogar ([Tesoura] [Papel] [Pedra]):')).strip().title()
if jogador == robo:
    print('Empate!')
elif jogador == 'Tesoura' and robo == 'Papel':
    print('Voce ganhou!')
elif jogador == 'Pedra' and robo == 'Tesoura':
    print('Voce ganhou!')
elif jogador == 'Papel' and robo == 'Pedra':
    print('Voce ganhou!')
elif robo == 'Tesoura' and jogador == 'Papel':
    print('Voce Perdeu!')
elif robo == 'Pedra' and jogador == 'Tesoura':
    print('Voce Perdeu!')
elif robo == 'Papel' and jogador == 'Pedra':
    print('Voce Perdeu!')
else:
    print('Jogada invalida!!!!')