num = int(input('Digite um numero [Use 999 para parar]:'))
cont = 0
total = 0 + num
while num != 999:
    num = int(input('Digite um numero [Use 999 para parar]:'))
    cont += 1
    total = total + num
if (total-900) < 0:
    print(f'Voce rodou 0 vezes com o valor de {num}')
else:
    print(f'O programa rodou {cont}, e somou no total {total-999}')