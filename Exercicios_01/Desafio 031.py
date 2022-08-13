from colorama import Fore, Style
viagem = float(input(Fore.GREEN+'Digite o tamanho da viagem: '))
if viagem > 200:
    print(Fore.LIGHTCYAN_EX+'O preço da viagem sera de: R${viagem*0.45}')
else:
    print(Fore.LIGHTBLUE_EX +f'O preço da viagem sera de: R${viagem*0.50}')