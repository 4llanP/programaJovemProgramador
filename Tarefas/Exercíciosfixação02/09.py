produto = {"nome": input('Nome: '), "preco": float(input('Valor: ')), "quantidade": int(input('Quantidade: '))}
#acesso/atribuição por chave, print()
print(f'O valor {produto['preco']}, com a quantidade {produto['quantidade']}, total: {(produto['preco']*produto['quantidade'])}')