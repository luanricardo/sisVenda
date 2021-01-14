print(' / LOJAS AMERICANAS / ' * 10)
print('=-=-' * 20)
preco = float(input('Preço das compras:'))
print('=-=-' * 20)
print('''FORMAS DE PAGAMENTO:
      [1] - À VISTA DINHEIRO/CHEQUE
      [2] - À VISTA NO CARTÃO
      [3] - 2x NO CARTÃO
      [4] - 3x OU MAIS NO CARTÃO
      [5] - APLICAR DESCONTO''')
print('=-=-' * 20)
opcao = int(input('ESCOLHA SUA OPÇÃO'))
print('=-=-' * 20)
if opcao == 1:
    total = preco - (preco * 10 /100)

elif opcao == 2:
    total = preco - (preco * 10/100)

elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra de R${total:.2f} será parcelada em 2x de R${parcela:.2f} no cartão')

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Qual a quantidade de parcelas ?'))
    parcela = total/totalparc
    print(f'Sua compra de R${preco:.2f}, com juros custara R${total:.2f} parcelado em {totalparc}x de R${parcela:.2f} no cartão')

elif opcao == 5:
    desc = float(input('Qual a porcentagem de desconto ?'))
    total = preco - (preco * desc / 100 )
    print(f'SUA COMPRA CUSTARA R${total:.2f}')

else:
    total = preco
    print('OPCÇÃO INVALIDA, TENTE NOVAMENTE!')

print(f'Sua compra de R${preco:.2f}, irá custar R${total:.2f} no final da compra')