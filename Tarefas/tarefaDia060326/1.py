# Leia saldo (float) e depósito (float). Use saldo += deposito e mostre o novo saldo.`
saldo = float(input('Informe o saldo: '))
print(f'Seu saldo é de: {saldo}')
deposito = float(input('Informe deposito: '))
saldo += deposito
print('Com o deposito vai para: {:.2f}'.format(saldo))

deposito = float(input('Informe segundo deposito: '))
saldo += deposito
print('Com o segundo deposito vai para: {:.2f}'.format(saldo))
