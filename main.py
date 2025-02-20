import Desafio_mercado
import pagamento

def mercado():
    nome = input('Digite seu nome: ')
    Desafio_mercado.display1(nome)
    produtos = ['0 - arroz','1 - feijao','2 - batata','3 - cafe','4 - frango']
    lista_valor = [32, 25, 8, 30, 20]
    m =  Desafio_mercado.carrinho(produtos,lista_valor)   
    print(m)
mercado()