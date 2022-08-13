import colorama
from colorama import Fore
metro = float(input(Fore.LIGHTMAGENTA_EX +'Digite quantos metros para converter para outras medidas: '))

print (Fore.WHITE + f'{metro}M são:')
print(f'{metro/1000} KM')
print(f'{metro/100:.2f} HM')
print(f'{metro/10} DAM')
print(f'{metro:.0f} M')
print(f'{metro*10:.0f} DM')
print(f'{metro*100:.0f} CM')
print(f'{metro*1000:.0f} MM')