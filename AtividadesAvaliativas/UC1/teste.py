import os

catalogo = [
    (1, 'arroz', 15.9),
    (2, 'feijao', 9.5),
    (3, 'macarrao', 4.2),
    (4, 'oleo', 6.9)
]

estoque = {
    '1': 20,
    '2': 35,
    '3': 50,
    '4': 15
}

carrinho = []

def exibir_catalogo():
    os.system('cls')
    print("\n {:=^20}".format('Catálogo'))
    for produto in catalogo:
        print(f"ID: {produto[0]} | Valor: {produto[2]:.2f} | Nome: {produto[1]}")

def cadastrar_produto():
    os.system('cls')
    produto_id = int(input('Id: '))
    nome = input('Nome: ')
    valor = float(input('Valor: '))
    quantidade = float(input('Quantidade: '))

    novo_produto = (produto_id, nome, valor)

    catalogo.append(novo_produto)
    estoque[str(produto_id)] = quantidade

def adicionar_carrinho(produto_id, quantidade):
    if str(produto_id) not in estoque:
        print("Produto não existe no estoque.")
        return

    if estoque[str(produto_id)] < quantidade:
        print("Sem estoque suficiente.")
        return

    produto = buscar_produto_por_id(produto_id)

    item = (produto_id, quantidade, produto[2])
    carrinho.append(item)

    estoque[str(produto_id)] -= quantidade

    print("Carrinho:", carrinho)

def devolver_item(produto_id):
    for item in carrinho:
        if item[0] == produto_id:
            estoque[str(produto_id)] += item[1]
            carrinho.remove(item)
            return

    print("Item não está no carrinho.")

def buscar_produto_por_id(produto_id):
    for produto in catalogo:
        if produto[0] == produto_id:
            return produto
    return None

def calcular_total():
    total = 0.0
    for item in carrinho:
        total += item[1] * item[2]
    return total

def aplicar_desconto():
    produto_id = int(input('Aplicar desconto no id: '))
    produto = buscar_produto_por_id(produto_id)

    if not produto:
        print("Produto não encontrado.")
        return

    desconto = float(input('Desconto (%): '))

    valor_antigo = produto[2]
    novo_valor = valor_antigo * (1 - desconto / 100)

    index = catalogo.index(produto)
    catalogo[index] = (produto[0], produto[1], novo_valor)

    print(f"Valor anterior: {valor_antigo:.2f}")
    print(f"Valor atual: {novo_valor:.2f}")


os.system('cls')
while True:
    print('\n1- ver protudos \n2- adicionar produto\n3- Adiciona carrinho\n4- Tira carrinho\n5- Aplica desconto')
    seleciona = int(input('Informe ação 0 encerra: '))
    if seleciona == 0:
        break
    match seleciona:
        case 1:
            exibir_catalogo()
        case 2:
            cadastrar_produto()
        case 3:
            adicionar_carrinho()
        case 4:
            devolver_item()
        case 5:
            aplicar_desconto()
        case _:
            print('Valor informado fora da lista, favor corrigir')