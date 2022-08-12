#
#numero = input('digite um numero: ')
#Não consegui :( , Da erro quando bota menos de 4 digitos:
#print(f'Milhar: {numero[0:1]}')
#print(f'Centena: {numero[1:2]}')
#print(f'Dezena: {numero[2:3]}')
#print(f'Unidade: {numero[3:4]}')
numero = int(input('Digite um numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

