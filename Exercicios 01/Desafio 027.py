nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print(f'Seu primeiro nome é: {lista[0]}')
print(f'O seu ultimo nome é: {lista[-1]}')