import colorama
from colorama import Fore, Style

km = float(input(Fore.LIGHTMAGENTA_EX+'Digite a velocidade: '))
if km > 80:
    print(Fore.YELLOW+'Velocidade acima do limite!')
    print(f'A multa foi de: {(km - 80) * 7}R$')
else:
    print(Fore.WHITE+'Velocidade abaixa do limite.')