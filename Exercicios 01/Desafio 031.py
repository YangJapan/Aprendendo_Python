viagem = float(input('Digite o tamanho da viagem: '))
if viagem > 200:
    print(f'O preço da viagem sera de: {viagem*0.45}')
else:
    print(f'O preço da viagem sera de: {viagem*0.50}')