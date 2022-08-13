from colorama import Fore, init
init()
numero = float(input(Fore.YELLOW+'Digite um numero: '))

print(Fore.YELLOW + f'O seu numero é {numero:.0f} o dobro dele é {numero*2:.0f} o seu triplo é {numero*3:.0f}', end=' ')
print(f'e sua raiz quadrada é {numero**(1/2):.2f}')