import random
robo = random.randint(0,10)
palpites = 1
print(robo)
print('Tente adivinhar o mesmo numero que um robo.')
pessoa = int(input('Digite um numero:'))
while pessoa != robo:
    if pessoa < robo:
        print('Maior... Tente novamente!')
    else:
        print('Menor... Tente novamente!')
    pessoa = int(input('Digite um numero:'))
    palpites += 1
print(f'Voce precisou de {palpites} para adivinhar!')
