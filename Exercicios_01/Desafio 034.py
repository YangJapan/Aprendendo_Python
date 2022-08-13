salario = float(input('Digite o seu salario: '))
if salario > 1250:
    print(f'O novo salario sera de: {(10 * salario / 100) + salario}R$')
else:
    print(f'O novo salario sera de: {(salario * 15 / 100) + salario}R$')