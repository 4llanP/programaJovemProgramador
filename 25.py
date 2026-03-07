# Leia base (float). Aplique *= 1.05 (aumento 5%), depois -= 2 (taxa), depois /= 2.
base = float(input('Informe: '))
print(f'Valor: {base}')
base *= 1.05
print(f'Valor: {base}')
base -= 2
print(f'Valor: {base}')
base /= 2
print(f'Valor: {base}')