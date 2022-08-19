total = 0
MaisVelhoHomem = 0
NomeDoVelho = ''
cont = 0
for i in range (1,5):
    print(f'----------{i} Pessoa----------')
    Nome = str(input('Nome: ')).strip()
    Idade = float(input('Idade: '))
    Sexo = str(input('Sexo [F/M]: ')).upper().strip()
    total += Idade
    media = total/4
    if Sexo == 'F' and Idade < 20:
        cont = cont + 1
    if i == 1 and Sexo == 'M':
        MaisVelhoHomem = Idade
        NomeDoVelho = Nome
    if Sexo == 'M' and Idade > MaisVelhoHomem:
        MaisVelhoHomem = Idade
        NomeDoVelho = Nome

print(f'A media é: {media}!')
print(f'O homem mais velho é o {NomeDoVelho.title()} com a idade de {MaisVelhoHomem}!')
print(f'Tem {cont} Mulheres menores de 20 anos!')