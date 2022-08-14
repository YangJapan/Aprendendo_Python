n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print('Reprovado!')
if media >= 5 and media < 6.9:
    print('Recuperação')
if media > 6.9:
    print('Aprovado')