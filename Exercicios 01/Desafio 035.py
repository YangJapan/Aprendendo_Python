r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if (r1 + r2) > r3:
    print('E possivel ter um triangulo!')
elif (r1 + r3 ) < r2:
    print('E possivel ter um triangulo!')
elif (r2 + r3) < r1:
    print('E possivel ter um triangulo!')
else:
    print('Não e possivel fazer um triangulo')