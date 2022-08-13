import colorama
from colorama import Fore, Style
import math
angulo = float(input(Fore.LIGHTBLACK_EX+'Digite o angulo que voce deseja:'))
seno = math.sin((math.radians(angulo)))
print(Fore.LIGHTRED_EX+ f'Angulo de {angulo} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'Angulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'Angulo de {angulo} tem a tangente de {tangente:.2f}')