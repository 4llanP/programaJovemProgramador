print('Soma todos os valores inseridos, para sair 0')
valor = 1
total = 0
while valor != 0:
    valor = float(input('Valor: '))
    total += valor
    print(f'Valor atual: {total:.1f}')
