preço = float(input('Digite o preço do produto: '))
escolha = int(input('Diga a forma de pagamento\n[ 1 ] - Dinheiro/Cheque 10% de desconto\n[ 2 ] - a vista no cartão 5% de desconto\n[ 3 ] - 2x no cartão preço normal\n[ 4 ] - 3x ou mais 20% de juros\n:'))
if escolha == 1:
    preço = ((preço * 10) / 100) - preço
    print(f'O preço final fica em {preço}')
elif escolha == 2:
    preço = ((preço * 5) / 100) - preço
    print(f'O preço final fica em {preço}')
elif escolha == 3:
    quantidade = int(input('Sera em quantas vezes? '))
    if quantidade > 2:
        print('Quantidade maior que 2, Favor selecionar opção de numero 4 na proxima vez', end=' ,')
        print('Saindo...')
    else:
        print(f'O preço final fica em {preço}')
elif escolha == 4:
    quantidade = int(input('Sera em quantas vezes? '))
    if quantidade < 3:
        print('Quantidade menor que 3, Favor selecionar opção de numero 3 na proxima vez', end=' ,')
        print('Saindo...')
    else:
        preço = ((preço * 20) / 100) + preço
        print(f'Sera {quantidade} vezes que vai dar {preço/quantidade} em {quantidade} vezes')
        print(f'O preço final fica em {preço}')

