import os
agenda = {"lana": "1111-1111", "bruno": "2222-2222"}

nome = input('Nome: ')
agenda[nome] = input('Número: ')
os.system('cls')


nome = input('Informe nome para atualizar: ')
if nome in agenda:
    agenda[nome] = input('Número atualizado: ')
else:
    print('Nome não está na agenda')


agenda.pop(input('\nRemover nome: '),0)
#agenda = dict(sorted((agenda.items())))
os.system('cls')


print('Nomes na lista: ', end='')
for i in agenda:
    print(i, end=' ')
print('\n',sorted(agenda.keys()))
print(agenda)