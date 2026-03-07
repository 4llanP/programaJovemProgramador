# Leia um número (int), aplique n %= 2 e imprima.
# 0 = par, 1 = ímpar
num = int(input('Informe um numero: '))
num %= 2
if num == 0:
    print('Numero par')
else:
    print('Numero impar')