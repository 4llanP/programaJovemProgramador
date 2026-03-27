import os
notastotal = []
os.system('cls')
for i in range(int(input('Quantidade de notas a inserir: '))):
    nota = float(input(f'Informe {i+1}º nota: '))
    if nota == -1:
        break
    notastotal.append(nota)
os.system('cls')

media = sum(notastotal)/len(notastotal)

if media < 7:
    print('Rodou, faz dnv')
else:
    print('Passou')
print(f'A media final: {media:.2f}\n')

for i in notastotal:
    print(f'Nota: {i}')