import colorama
from colorama import Fore, Style
import random
robo = random.randint(0,5)
usuaria = int(input(Fore.LIGHTGREEN_EX+'Digite um numero de 1 a 5: '))
if robo == usuaria:
    print(Fore.BLUE+'Voce acertou o mesmo numero do robo!')
else:
    print(Fore.RED+'Voce não acerto o mesmo numero do robo!')
