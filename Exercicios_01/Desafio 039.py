import datetime
ano = datetime.date.today().year
nascimento = int(input('Digite sua data de nascimento:'))
print(f'Sua idade é de :{ano - nascimento}')

if ano - nascimento < 18:
    print('Ainda não precisa se alistar!')
    print(f'Faltam {ano-nascimento - 18} anos para se alistar')
elif ano - nascimento == 18:
    print(f'Precisa se alistar esse ano: {ano}')
elif ano - nascimento > 18:
    print('Ja passou a hora de se alistar!')
    print(f'Passou {ano-nascimento-18} anos para se alistar!')
    print(f'Devia ter se alistado em:{((ano-nascimento-18) - ano )* -1 }')