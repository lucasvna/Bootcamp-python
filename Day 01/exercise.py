estoque = []

num = int(input('Digite o número de produtos que quer cadastrar: '))

for i in range(num):
    nome = input('Digite o nome do produto: ')
    qtdEstoque = int(input('Digite a quantidade em estoque: '))
    valor = float(input('Digite o valor do produto: '))
    produto = {nome, qtdEstoque, valor}
    estoque.append(produto)

    qtde_vendida = int(input('Digite a quantidade a ser vendida: '))

    if qtde_vendida > qtdEstoque:
        print('Não pode realizar a venda.')

    else:
        valor_pago = float(input('Digite o valor pago'))
        realizarVenda(qtde_vendida, valor_pago, produto)

def realizarVenda(qtde_vendida, valor_pago, produto):
    if qtde_vendida > qtdEstoque:
        print('Quantidade insuficiente em esstoque.')
    else:
        valor_total = qtde_vendida * valor
        if valor_pago >= valor_total:
            troco = valor_pago - valor_total
            