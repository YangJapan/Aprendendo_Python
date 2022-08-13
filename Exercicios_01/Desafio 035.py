from colorama import Fore, Style
r1 = float(input(Fore.WHITE+'Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print(Fore.CYAN+ 'É possivel formar um triangulo!')
else:
    print('Não é possivel formar um triangulo!')