tot = 1
num = int(input('Digite um numero: '))
total = 0
maior = num
menor = num
totale = total + num
resp = str(input('Quer continuar[S/N]: ')).upper()
while resp == 'S':
    num = int(input('Digite um numero: '))
    resp = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    tot += 1
    totale = totale + num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'Foram digitados {tot} numeros é a media foi de {totale/tot:.2f}')
print(f'Menor {menor}\nMaior {maior}')