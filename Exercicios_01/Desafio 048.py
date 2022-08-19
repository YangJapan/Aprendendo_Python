cont = int(input('Digite quantas vezes deseja fazer: '))
soma = 0
for c in range (1,cont, 2):
    if c % 3 == 0:
        soma = soma + c
print(f'O valor de todas as somas é de : {soma}')