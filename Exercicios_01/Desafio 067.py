print('*-' * 30)
num = int(input('Digite um valor para ver a tabuada: '))
cont = 1
while num >= 0:
    print('*-' * 15)
    while cont < 11:
        print(f'{num} * {cont} = {num*cont}')
        cont += 1
    print('*-' * 15)
    num = int(input('Digite um valor para ver a tabuada: '))
    cont = 1
print('Tabuada finalizada!')

