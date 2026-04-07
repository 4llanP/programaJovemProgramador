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
    print("\n=== CATÁLOGO ===")
    for produto in catalogo:
        print(f"ID: {produto[0]} | Valor: {produto[2]:.2f} | Nome: {produto[1]}")


def buscar_produto_por_id(produto_id):
    for produto in catalogo:
        if produto[0] == produto_id:
            return produto
    return None


def cadastrar_produto():
    produto_id = int(input('Id: '))
    nome = input('Nome: ')
    valor = float(input('Valor: '))
    quantidade = float(input('Quantidade: '))

    novo_produto = (produto_id, nome, valor)

    catalogo.append(novo_produto)
    estoque[str(produto_id)] = quantidade


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


def adicionar_ao_carrinho(produto_id, quantidade):
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


def calcular_total():
    total = 0.0
    for item in carrinho:
        total += item[1] * item[2]
    return total


# ================== EXECUÇÃO ==================

os.system('cls')

print('=' * 50)
print('Cadastrar produto')
cadastrar_produto()

os.system('cls')

print('=' * 50)
exibir_catalogo()

print('=' * 50)
aplicar_desconto()

print('=' * 50)
print(f'Estoque atual: {estoque}')

print('\nAdicionar ao carrinho')
adicionar_ao_carrinho(int(input('Id: ')), float(input('Quantidade: ')))

print('=' * 50)

print('Adicionar ao carrinho')
adicionar_ao_carrinho(int(input('Id: ')), float(input('Quantidade: ')))

print('=' * 50)
print(f'Estoque atual: {estoque}')

print('=' * 50)
print('Devolução')
devolver_item(int(input('Id: ')))

os.system('cls')

print('Seu carrinho:', carrinho)
print(f'Estoque atual: {estoque}')

total = calcular_total()
print(f'\nTotal a pagar: {total:.2f}')

print('Catálogo ordenado por preço:', sorted(catalogo, key=lambda produto: produto[2]))