notas = [float(input('Nota: ')),float(input('Nota: ')),float(input('Nota: '))]
print(f'Media: {(sum(notas))/3:.1f}')

notas[notas.index(min(notas))] = float(input(f'Subistituto {min(notas)}: '))
print(notas)
print(f'Nova media: {(sum(notas))/3:.1f}')