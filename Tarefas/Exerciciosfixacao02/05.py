fila = ["Ana", "Bruno"]
print(fila)

fila.extend([input('Nome: '), input('Nome: ')])
print(fila)

fila.insert(0, input('Prioritario: '))
print(fila)

fila.pop(fila.index(input('Atendido: ')))
print(fila)
