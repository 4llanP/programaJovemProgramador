print('Soma todos os valores inseridos, para sair 0')
total = []
while True:
    valor = float(input('Valor: '))
    if valor == 0:
        break
    total.append(valor)

print(f'Valor total: {sum(total):.1f}\nMedia: {sum(total)/len(total)}\nTotal de compras: {len(total)}')
