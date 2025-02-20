def display1(nome):
    print()
    print('Olá seja bem vindo', nome)

def carrinho(produtos,precos):
    meu_carrinho = []
    valores = []
    p = (input('Gostaria de fazer seu pedido? '))
    while p == 'sim':
        print('\n0 - arroz','\n1 - feijao','\n2 - batata','\n3 - cafe','\n4 - frango')
        print()
        pedido = int(input('Realize o seu pedido >> '))
        meu_carrinho.append(pedido)
        valores.append(precos[pedido])
        soma = sum(valores)
        print(soma)
        p =  input('Gostaria de pedir algo mais? ')
    return meu_carrinho

