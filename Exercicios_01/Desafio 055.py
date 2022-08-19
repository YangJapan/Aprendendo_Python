maior = 0
menor = 0
for p in range (1,6):
    peso = float(input(f'Digite o peso da {p} pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\nO maior foi {maior}KG')
print(f'O menor foi {menor}KG')