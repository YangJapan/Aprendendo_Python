#escolha != 1 or escolha != 2 or escolha != 3 or escolha != 4 or escolha != 5:
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
escolha = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa\n:'))
if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
    print('Numero invalido!')
while escolha == 4:
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite um outro numero: '))
    escolha = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa\n:'))
if escolha == 1:
    print(f'{num1} + {num2} = {num1+num2}')
elif escolha == 2:
    print(f'{num1} x {num2} = {num1*num2}')
elif escolha == 3:
    if num1 > num2:
        print(f'O maior numero é {num1}')
    elif num2 > num1:
        print(f'O maior numero é {num2}')
    elif num2 == num1:
        print('Os dois numeros são iguais.')
elif escolha == 5:
    print('Saindo...')