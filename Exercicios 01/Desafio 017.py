from math import sqrt
cateto1 = float(input('Digite o cateto: '))
cateto2 = float(input('Digite o cateto: '))
hipotenusa = (cateto1 ** 2) + (cateto2 ** 2)
raiz = sqrt(hipotenusa)
print(f'O comprimento da hipotenusa é de: {raiz:.2f} ')