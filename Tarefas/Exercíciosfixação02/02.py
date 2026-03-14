numeros = [int(input('Valor: ')),int(input('Valor: ')),int(input('Valor: ')),int(input('Valor: '))]
print(len(numeros))
remover = int(input('Remova: '))
if remover in numeros:
    numeros.remove(remover)
    print(numeros)
print(len(numeros))
