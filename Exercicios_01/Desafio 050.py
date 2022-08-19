soma = 0
for n in range (0,6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma = soma + num
print(soma)