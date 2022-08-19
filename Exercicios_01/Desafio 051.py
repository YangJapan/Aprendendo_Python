inicio = int(input('Digite o valor de inicio: '))
termo = int(input('Digite a razão: '))
decimo = inicio + (10 - 1) * termo
for c in range (inicio,decimo + termo,termo):
    print(c,end=' -> ')
print('Acabou')