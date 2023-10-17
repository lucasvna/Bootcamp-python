mercadorias = []
produto = input('Qual produto deseja cadastrar? Ex.: café, biscoito: ')
valorProduto = float(input('Qual o valor do produto? '))
marca = input('Qual a marca do produto? ')
estoque = int(input('Quantos produtos disponíveis em estoque? '))

cadastro = (produto, valorProduto, marca, estoque)
mercadorias.append(cadastro)

def troco(valor, compra):
    troco = compra - valorProduto
    return troco

total = int(input('Quantos produtos quer comprar? '))
compra = valorProduto * estoque

if total >  estoque:
    print(f'Erro! Voce solicitou {total} produtos e há apenas {estoque} no estoque')

dinheiro = float(input('Com quantos reais você vai pagar esta compra? '))

# if dinheiro > compra:
#     print(f'Seu troco é {troco}')

else:
    print('aaaa')