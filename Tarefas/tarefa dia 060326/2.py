# Leia um contador (int) e um passo (int). Faça contador += passo duas vezes. Mostre o resultado.


contador = int(input('Informe o contador: '))
passos = int(input('Quantidade de passos: '))
contador += passos *2
print(f'Quantidade de passos no conatdo: {contador}')
