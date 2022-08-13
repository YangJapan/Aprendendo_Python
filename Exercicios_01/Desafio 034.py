from colorama import Fore, Style
salario = float(input(Fore.LIGHTMAGENTA_EX+'Digite o seu salario: '))
if salario > 1250:
    print(Fore.BLUE +f'O novo salario sera de: {(10 * salario / 100) + salario}R$')
else:
    print(Fore.YELLOW + f'O novo salario sera de: {(salario * 15 / 100) + salario}R$')