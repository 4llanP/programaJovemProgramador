Cordenadas = (10, 20)
dias = ('segunda','terça','quarta','quinta','sexta')

print(f'X: {Cordenadas[0]} \nY: {Cordenadas[1]}')

print(f'Primeiros 3 dias: {dias[:3]}') # pega o quarto valor da tupla
print(f'tamanho tupla dias: {len(dias)}') #ultimo valor da tupla
print(f'Tem segunda? ', 'segunda' in dias) #Valida se 'segunda ' existe na tupla 
print(f'Contagem de terça: {dias.count('terça')}') # Conta quantas terças tem
print(f'Posição (indice) quarta: {dias.index('quarta')}') # localiza index da quarta, no caso ta na posicao 2