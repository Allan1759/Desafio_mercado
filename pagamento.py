def pagamentos_1():
    print('1  - PIX | 2 -  Cartão credito | 3 - Cartão Debito | 4 -  DINHEIRO')
    formas =  ['pix', 'cc','cd','dinheiro']
    pag = int(input('Digite a opção de pagamento: '))
    if pag == 0:
       print('FORMA DE PAGAMENTO:')
       print(formas[pag])
       print()
       print('Obrigada volte sempre')
    elif pag == 1:
       print('FORMA DE PAGAMENTO:')
       print(formas[pag])
       print()
       print('Obrigada volte sempre')
    elif pag == 2:     
       print('FORMA DE PAGAMENTO:')
       print(formas[pag])  
       print()  
       print('Obrigada volte sempre')
    elif pag== 3:
       print('FORMA DE PAGAMENTO:')
       print(formas[pag])
       print()
       print('Obrigada volte sempre')
    else:
       print('Essa forma não existe')
