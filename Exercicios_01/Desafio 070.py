resp = 'S'
total = 0
MaisMil = 0
print('*-' * 30)
print('Cadastre produtos!')
print('*-' * 30)
nome = str(input('Nome do produto: '))
preço = float(input('Preço: R$'))
nomebarato = nome
barato = preço
if preço > 1000:
    MaisMil += 1
total += preço
resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
while resp != 'S' and resp != 'N':
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

while resp == 'S':
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    if preço < barato:
        nomebarato = nome
        barato = preço
    if preço > 1000:
       MaisMil += 1
    total += preço
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        print('Finalizando...')
        break
print(f'O total foi de {total}!')
print(f'Temos {MaisMil} produtos maiores de R$1000')
print(f'O mais produto mais barato foi {nomebarato.title()} é custa R${barato}')
