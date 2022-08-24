import random
print('*-' * 12)
print('Jogo de par ou impar!')
print('*-' * 12)
while True:
    robo = random.randint(0, 10)
    num = int(input('Digite um numero: '))
    if num > 10:
        print('Coloque um valor menor na proxima vez[10 Maximo]! Saindo...')
        break
    Impar = str(input('Impar ou Par [P/I]')).upper().strip()[0]
    if Impar != 'P' and Impar != 'I':
        print('Escolha não valida! Saindo...')
        break
    soma = robo + num
    if soma % 2 == 0 and Impar == 'P':
        print('Voce ganhou, Jogue mais uma vez!')
        print(f'A soma foi de {soma}')
    elif soma % 2 != 0 and Impar == 'P':
        print('Voce perdeu!')
        print(f'A soma foi de {soma}')
        break
    elif soma % 2 != 0 and Impar == 'I':
        print('Voce ganhou, Jogue mais uma vez!')
        print(f'A soma foi de {soma}')
    elif soma % 2 == 0 and Impar == 'I':
        print('Voce perdeu!')
        print(f'A soma foi de {soma}')
