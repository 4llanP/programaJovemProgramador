import os
def exibe():
    print(f'Produtos: {catalogo[0][1]},{catalogo[1][1]},{catalogo[2][1]},{catalogo[3][1]},{catalogo[-1][1]}')
    print(f'Ids (ordem acima): {catalogo[0][0]},{catalogo[1][0]},{catalogo[2][0]},{catalogo[3][0]},{catalogo[-1][0]}')
def procuraId(id):
    for x in catalogo:
        if x[0] == id:
            return x
    return
def cadastra():
    id = int(input('Id: '))
    novoProduto = (id, input('Nome: '), float(input('Valor: ')))
    quantidade = float(input('Quantidade: '))
    estoque[str(id)] = quantidade
    catalogo.append(novoProduto)
    return
def aplicaDesconto():
    x = procuraId(int(input('Aplicar desconto id: ')))
    desconto = float(input('Deconto (sem %): '))
    print('\nValor anterior: ',x[2])
    catalogo[catalogo.index(x)] = (x[0],x[1], x[2]*(desconto/100))
    x = (x[0],x[1], x[2]*(desconto/100))
    print(f'Valor atual: {catalogo[catalogo.index(x)][2]:.2f}')    
    return
def compras(id, quantidade):
    if estoque[str(id)] >= quantidade:
        compras = (id, quantidade, procuraId(id)[2])
        carrinho.append(compras)
        estoque[str(id)] -= quantidade
        print('Carrinho: ', carrinho)
    else:
        print('Sem estoque suficiente')
    return
def devolucao(id):
    for item in carrinho:
        if item[0] == id:
            estoque[str(id)] += carrinho[carrinho.index(item)][1]
            carrinho.pop(carrinho.index(item))
            return
    return print('Item nao esta no carrinho')
catalogo = [
    (1,'arroz',15.9),
    (2,'feijao',9.5),
    (3,'macarrao',4.2),
    (4,'oleo',6.9)
]
estoque = {
    '1': 20,
    '2': 35,
    '3': 50,
    '4': 15
}
carrinho = []


os.system('cls')
print('='*100,'\nCadastre produto ')
cadastra()
os.system('cls')

''' PRINTS SOLICITADOS NO EXERCICIOS, COMENTEI PARA NÃO POLUIR A SAÍDA NO CONSOLE
exibe()
print('Cadestre produtos: ')
cadastra()
os.system('cls')
print('Cadestre produtos: ')
cadastra()
os.system('cls')
print(catalogo)
print(type(catalogo))
print('='*100)
print(estoque)
print(type(estoque))
print('='*100)'''

print('='*100)
exibe()
print('='*100)
aplicaDesconto()
print('='*100)
print(f'Estoque atual: {estoque}')
print('\nAdicione ao carrinho ')
compras(int(input('Id: ')), float(input('Quantidade: ')))
print('='*100)
print('Adicione ao carrinho ')
compras(int(input('Id: ')), float(input('Quantidade: ')))
print('='*100)
print(f'Estoque atual: {estoque}')
print('='*100)
print('Devolução: ')
devolucao(int(input('Id: ')))
os.system('cls')
print('Seu carrinho: ', carrinho)
print(f'Estoque atual: {estoque}')

total = 0.0
for x in carrinho:
    total += x[2]*x[1]
print(f'\nTotal a pagar: {total:.2f}')    

print('Catalogo: ', sorted(catalogo, key=lambda x: x[2]))