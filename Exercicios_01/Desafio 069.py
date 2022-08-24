continuar = 'S'
contIdade = 0
contMascu = 0
contIdaFemi = 0
while continuar == 'S':
    print('*-' *15)
    print('Cadastre um pessoa!')
    print('*-' * 15)
    idade = int(input('Digite a idade da pessoa: '))
    if idade >= 18:
        contIdade += 1
    sexo = str(input('Qual o sexo [M/F]:')).upper().strip()[0]
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Qual o sexo [M/F]:')).upper().strip()[0]
    if sexo == 'M':
        contMascu += 1
    if sexo == 'F' and idade < 20:
        contIdaFemi += 1
    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
print(f'No final do programa tivemos {contMascu} Homens, {contIdade} Pessoas maiores de 18 anos é {contIdaFemi} Mulheres menores de 20 anos!')
