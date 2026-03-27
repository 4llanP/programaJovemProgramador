inventario = []
while True:
    item = input('Item encontrado: ')
    if item == 'sair':
        break
    inventario.append(item)

inventario.sort()

print(f'Inventário: {inventario}')
print(f'Total de itens: {len(inventario)}')