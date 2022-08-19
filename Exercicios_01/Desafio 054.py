contM = 0
contn = 0
from datetime import date
ano = date.today().year
for c in range (1,8):
    pessoa = int(input(f'Em que ano a {c} pessoa nasceu: '))
    idade = ano - pessoa
    if idade >= 18:
        contM += 1
    else:
        contn += 1
print(f'Tem {contM} maiores de idades é {contn} menores')