primeiro = int(input('Digite um numero inicial: '))
razao = int(input('Digite a razão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{primeiro}', end=' -> ')
        primeiro += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'{total} termos mostrados!')