# Leia vidas (int) e perdidas (int). Use vidas -= perdidas.
vidas = int(input('Número de vidas: '))
dano = int(input('Dano recebido: '))

vidas -= dano
print(f'Vida atual: {vidas}')