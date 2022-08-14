import datetime
nascimento = int(input('Digite o ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - nascimento
if idade <= 9:
    print('Mirim!')
elif idade <= 14:
    print('Infantil!')
elif idade <= 19:
    print('Junior!')
elif idade <= 20:
    print('Senior')
elif idade > 20:
    print('Master!!!')