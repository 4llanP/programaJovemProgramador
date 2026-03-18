aluna = {'id': 1, 'nome': 'Alamo', 'nota':9.2}
pessoa = {'nome': 'Ana', 'idade': 25}

#chama
print(f'Nome da pessoa: {pessoa['nome']}')

#incrementa
pessoa['Cidade'] = 'florianopolix'
pessoa['idade'] = 26
print(f'Pessoa atualizada: {pessoa}')


removido = pessoa.pop('idade') #pega a idade e coloca em removido
print(f'Valor removido (idade): {removido}')
print(f'Após pop(idade): {pessoa}')

print(f'Qautnidade de aluna: {len(aluna)}')

print(f'Nomes de aluna: {list(aluna.keys())}')
print(f'Valores de aluna: {list(aluna.values())} ')
print(f'Itens de aluna: {list(aluna.items())}')

print(f'Chave nota existe? {'nota' in aluna}')

print(f'Turma (com default): {aluna.get('turma', 'não cadastrada')}')

aluna.update({'nota': 9.5, 'turma':'a'})
print(f'Aluna após uptade: {aluna}')

for chave, valor in aluna.items():
    print(f'{chave} -> {valor}')
