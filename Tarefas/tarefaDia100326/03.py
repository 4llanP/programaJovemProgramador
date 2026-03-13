Cordenadas = (10, 20)
dias = ('segunda','terça','quarta','quinta','sexta')

print(f'X: {Cordenadas[0]} \nY: {Cordenadas[1]}')

print(f'Primeiros 3 dias: {dias[:3]}')

print(f'tamanho tupla dias: {len(dias)}')

print(f'Tem segunda? ', 'segunda' in dias)

print(f'Contagem de terça: {dias.count('terça')}')
print(f'Posição (indice) quarta: {dias.index('quarta')}')