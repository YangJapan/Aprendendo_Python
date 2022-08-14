valor = float(input('Digite o valor da casa: '))
salariomensal = float(input('Digite o seu salario mensal: '))
tempo = float(input('Digite em quanto tempo voce ira pagar: '))

limite = ((salariomensal * 30) /100)
prestaçãoanual = valor / tempo
prestaçãomensal = prestaçãoanual / 12

if prestaçãomensal < limite:
    print('Emprestimo garantido!')
else:
    print('Emprestimo negado!')
print(f'Seu limite é de : {limite}')
print(f'O valor da prestação anualmente sera de: {prestaçãoanual:.2f}')
