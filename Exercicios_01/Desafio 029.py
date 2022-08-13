km = float(input('Digite a velocidade: '))
if km > 80:
    print('Velocidade acima do limite!')
    print(f'A multa foi de: {(km - 80) * 7}R$')
else:
    print('Velocidade abaixa do limite.')