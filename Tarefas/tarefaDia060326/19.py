# Leia estoque (int). Subtraia venda com -=, depois reposição com +=, por fim %= 6.
estoque = int(input('Estoque: '))
vendas = int(input('Vendas: '))
reposicao = int(input('Reposicao: '))
estoque -= vendas
estoque += reposicao
estoque %= 6

print(f'Estoque final: {estoque}')