# Leia tempo em segundos (int). Converta para minutos inteiros com //= 60 e depois use %= para obter segundos restantes.
segundos = int(input('Segundos: '))
sobra = segundos
segundos //= 60
sobra %= 60
print(f'Total de {segundos} minutos e {sobra} segundos')