sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    print('Sexo invalido!')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo valido!')
print('Saindo...')