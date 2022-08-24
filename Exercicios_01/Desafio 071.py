print('='* 30)
print(f'{"Banco CEV":^30}')
print('='* 30)
valor = int(input('Qual valor voce quer sacar? R$'))
total = valor
ced = 200
totalCedulas = 0
while True:
    if total >= ced:
        total -= ced
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cedulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCedulas = 0
        if total == 0:
            break