numeros = []
for i in range(10):
    numeros.append(float(input(f'Informe {i+1}° número: ')))
    if numeros[i] > 10:
        print('Maior que 10')
    elif numeros[i] == 10:
        print('Igual a 10')
    else:
        print('Menor que 10')
