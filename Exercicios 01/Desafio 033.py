n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o ultimo numero: '))

if n1 > n2 and n1 > n3:
    print(f'O maior é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior é {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior é {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor é {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor é {n3}')