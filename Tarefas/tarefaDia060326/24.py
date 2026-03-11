# Leia metros (int). Converta para km inteiros com //= 1000 e guarde metros restantes com %= (em outra variável).
metros = int(input('Metros: '))
sobra = metros
sobra %= 1000
metros //= 1000
print(f'Total de {metros}km e {sobra} metros')