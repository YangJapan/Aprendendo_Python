palavra = str(input('Digite uma frase: ')).strip().upper()
print(f'Sua palavra tem {palavra.count("A")}')
print(f'A primeira letra A aparece na casa de numero: {palavra.find("A") + 1}')
print(f'A ultima letra A aparece na casa de numero: {palavra.rfind("A") + 1}')
print(f'A frase escrita foi: {palavra.title()}')
