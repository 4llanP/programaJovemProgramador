frutas = ['maça', 'banana', 'uva']
numeros = [1,2,3,4]

#Acessar elementos
print(f'Primeira fruta: {frutas[0]}')
print(f'Ultima fruta: {frutas[-1]}') #-1 busca a ultima da lista, indifernete do tamanho
print(f'Penultima fruta: {frutas[-2]}')

frutas[1] = 'Banana nanica'
print(f'Após alterar: {frutas}')

frutas.append('morango')
frutas.insert(1,'pera')
print(f'Após alterar: {frutas}')

frutas.remove('uva')
ultima = frutas.pop()
print(f'Após alterar: {frutas}')

print(f'Tamanho da lista : {len(frutas)}')
print(f'Fatiamento [0:2]: {frutas[0:2]}')
print(f'Confere, exemplo maça: ', 'maça' in frutas)

print('Lista original: ', numeros)
print('Soma: ', sum(numeros))
print('Maior: ', max(numeros))
print('Menor: ', min(numeros))
numeros.reverse()
print('Reversa: ', numeros)
numeros.sort()
print('Ordenar crescente', numeros)
numeros.sort(reverse=True)
print('Ordernar decrescente', numeros)


for i in frutas:
    print('Fruta: ', i)

quadrados = [n * n for n in [1,2,3,4,5]]
print('Quadrados: ', quadrados)