# Leia estoque (int) e vendidas (int). Atualize com -= e mostre o estoque final.
estoque = int(input('Informe o estoque: '))
vendas = int(input('Quantidade de vendas: '))

estoque -= vendas
print(f'Seu estoque atual: {estoque}')