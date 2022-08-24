cont = soma = 0
while True:
    num = int(input('Digite um numero inteiro [999 Para Parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos valores foi de {soma}, Foram digitados {cont} valores!')
