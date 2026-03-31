a = float(input('1° valor: '))
b = float(input('2° valor: '))
tipo = input('Informe operação usando o simbolo (+, -, /, *)')

if tipo == '+':
    print(a+b)
elif tipo == '-':
    print(a-b)
elif tipo == '/':
    print(a/b)
else:
    print(a*b)