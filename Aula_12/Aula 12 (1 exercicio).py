nome = str(input('Digite seu nome: ')).title().strip()
if nome == 'Yang':
    print('Belo nome!')
elif nome == 'Ninguem':
    print('E o senhor ninguem!')
else:
    print('Nome bem normal.')
print(f'Tenha um bom dia {nome}')