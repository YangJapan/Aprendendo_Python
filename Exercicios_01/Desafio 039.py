import datetime
ano = datetime.date.today().year
nascimento = int(input('Digite sua data de nascimento:'))
if ano - nascimento < 18:
    print('Ainda não precisa se alistar!')
elif ano - nascimento == 18:
    print(f'Precisa se alistar esse ano: {ano}')
elif ano - nascimento > 18:
    print('Ja passou a hora de se alistar!')