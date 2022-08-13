from colorama import Fore, Style
import datetime
ano = int(input(Fore.LIGHTWHITE_EX+'Digite o ano para saber se é ou não bissexto: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(Fore.BLACK + f'{ano} é um ano bissexto!')
else:
    print(Fore.LIGHTBLACK_EX + f'{ano} Não é um ano bixesto!')