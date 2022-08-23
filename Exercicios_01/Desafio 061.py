num = int(input('Digite o valor inicial: '))
termo = int(input('Digite a razão: '))
new = num + termo
tot = 0
print(f'{num}', end=' -> ')
while tot < 9:
    tot += 1
    print(f'{new}',end=' -> ')
    new = new + termo
print('Acabou')
