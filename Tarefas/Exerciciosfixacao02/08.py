produto = {"nome": str, "preco": float, 'deconto': float}
produto1 = {"nome": str, "preco": float,}

print(produto, produto1)
produto.pop('deconto', 0)
produto1.pop('deconto', 0)
print(produto, produto1)
