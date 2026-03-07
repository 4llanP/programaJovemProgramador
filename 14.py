# Leia dias (int). Mantenha apenas os dias restantes após converter para semanas (7 dias) usando %=.
dias = int(input('Quantidade dias: '))
dias %= 7
print(f'Total de dias restantes apos convertes em semanas: {dias}')