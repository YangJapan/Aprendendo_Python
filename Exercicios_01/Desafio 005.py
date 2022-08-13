from colorama import Fore, init
init()
numero = int(input(Fore.GREEN+'Digite um numero: '))

print(Fore.LIGHTRED_EX+ f'O numero digitado foi {numero} o seu sucessor é {numero+1} é seu antecessor é {numero-1}')