frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for i in range (len(junto) -1, -1 , -1):
    inverso += junto[i]
if inverso == junto:
    print('E um palindromo!')
else:
    print('Não e um palindromo!')