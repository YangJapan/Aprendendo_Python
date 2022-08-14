from colorama import Fore, Style
r1 = float(input(Fore.WHITE+'Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print(Fore.CYAN+ 'É possivel formar um triangulo!')
    if r1 != r2 and r2 != r3:
        print('Triangulo escaleno!')
    elif r1 == r2 and r2 != r3 or r2 == r3 and r2 != r1:
        print('Triangulo isosceles!')
    elif r1 == r2 and r2 == r3:
        print('Triangulo Equilatero!')
else:
    print(Fore.CYAN+ 'Não é possivel formar um triangulo!')