from colorama import Fore, init
init()
n1 = float(input(Fore.YELLOW +'Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print(Fore.LIGHTGREEN_EX + f'A primeira nota foi de {n1:.2f}', end=' ')
print(f'A segunda nota foi de {n2:.2f}', end=' ')
print(f'A media foi de {(n1+n2)/2:.2f}', end=' ')