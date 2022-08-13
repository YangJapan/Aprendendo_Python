from colorama import Fore, init
init()
digito = input(Fore.GREEN + 'Digite algo para saber informaçoes: ')

print(Fore.LIGHTCYAN_EX + 'O seu tipo é: ', type(digito))
print('So tem espaços: ', digito.isspace())
print('E alfabetico: ', digito.isalpha())
print('E numero: ', digito.isnumeric())
print('E alfanumerico: ', digito.isalnum())
print('Esta em maiúsculas: ', digito.isupper())
print('Esta em minusculas: ', digito.islower())
print('Esta capitalizada: ', digito.istitle())