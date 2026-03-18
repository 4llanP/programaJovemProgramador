frutas = ['maça', 'banana', 'aqui', 'uva']
numeros = [1,2,3,4]

#Acessar elementos
print(f'Primeira fruta: {frutas[0]}')
print(f'Ultima fruta: {frutas[-1]}') #-1 busca a ultima da lista, indifernete do tamanho
print(f'Penultima fruta: {frutas[-2]}') #-2 antepenultima

frutas[1] = 'Banana nanica' # adicionar na posicao 1 'banana nanica'
print(f'Após alterar: {frutas}')

frutas.append('morango') #Adiciona no final
frutas.insert(1,'pera') #Adiciona na posicao <1>, pera (posicao, valor)
print(f'Após alterar: {frutas}')

frutas.remove('uva') #Remove 'uva'
ultima = frutas.pop() #Pega ultima, tira do frutas e ultima recebe
print(ultima)
print(f'Após alterar: {frutas}')

print(f'Tamanho da lista : {len(frutas)}') # Tamanho da lista
print(f'Fatiamento [0:2]: {frutas[0:2]}') # Separa frutas [contador]
print(f'Confere, exemplo maça: ', 'maça' in frutas) # in confere se existe

print('Lista original: ', numeros)
print('Soma: ', sum(numeros)) # soma
print('Maior: ', max(numeros)) # maior
print('Menor: ', min(numeros)) # menor
numeros.reverse() # reverte
print('Reversa: ', numeros)
numeros.sort() # ajusta crescente
print('Ordenar crescente', numeros)
numeros.sort(reverse=True) # ajusta decrescente
print('Ordernar decrescente', numeros)

# in valida se existe, no caso i = posicao 1, 2, 3...
for i in frutas:
    print('Fruta: ', i)

#para cada valor na lista [] N é (0, 1, 2....) * ele mesmo, chegando no valor ao quadrado
quadrados = [n * n for n in [1,2,3,4,5]]
print('Quadrados: ', quadrados)