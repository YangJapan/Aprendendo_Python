ano = int(input('Digite o ano para saber se é ou não bixesto: '))
if ano % 4 == 0:
    print(f'{ano} é um ano bixesto!')
else:
    print('Não é um ano bixesto!')