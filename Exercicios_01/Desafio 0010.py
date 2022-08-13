import colorama
from colorama import Fore, Style
real = float(input(Fore.LIGHTYELLOW_EX+'Digite a quantidade de reais para saber a contação das principais moedas: R$'))
print(Fore.GREEN + f'A quantidade de dolares é de: {real/5.16:.2f}')
print(f'A quantidade de euros é de: {real/5.32:.2f}')
print(f'A quantidade em libras esterlinas é de: {real/6.29:.2f}')
print(f'A quantidade em Ienes japoneses é de: {real*25.78:.2f}')
print(f'a quantidade de dolares australianos é de: {real/3.67:.2f}')