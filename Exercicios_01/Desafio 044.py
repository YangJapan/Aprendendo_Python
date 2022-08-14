preço = float(input('Digite o preço do produto: '))
escolha = int(input('Diga a forma de pagamento\n1- Dinheiro/Cheque 10% de desconto\n2- a vista no cartão 5% de desconto\n3- 2x no cartão preço normal\n4- 3x ou mais 20% de juros\n:'))
if escolha == 1:
    preço = ((preço * 10) / 100) - preço
    print(f'O preço final fica em {preço}')
elif escolha == 2:
    preço = ((preço * 5) / 100) - preço
    print(f'O preço final fica em {preço}')
elif escolha == 3:
    print(f'O preço final fica em {preço}')
elif escolha == 4:
    preço = ((preço * 20) / 100) + preço
    print(f'O preço final fica em {preço}')

