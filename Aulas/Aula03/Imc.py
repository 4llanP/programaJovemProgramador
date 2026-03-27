nome = input('Informe seu nome: ')
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura (em metros): '))

imc = peso / (altura**2)
print(f'O IMC do {nome}: {imc:.2f}')

if imc < 18.5:
    print('Baixo peso')
elif (imc >= 18.5) and (imc < 25):
    print('Normal')
elif (imc >= 25) and (imc < 30):
    print('Sobrepeso')
else: 
    print('feliz')