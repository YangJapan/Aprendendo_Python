import colorama
from colorama import Fore, Style
largura = float(input(Fore.WHITE+'Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = altura * largura
UmLitro = area / 2
print(Fore.CYAN + f'Voce ira precisar de {UmLitro:.2f} litros de tinta para pintar {area} m²')