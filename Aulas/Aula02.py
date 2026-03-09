import os

def div(x, y):
    z = x/y
    return z
def mult(x, y):
    z = x*y
    return z
def soma(x, y):
    z = x+y
    return z
def sub(x, y):
    z = x+y
    return z
def med(x,y,z):
    w = (x+y+z)/3
    return w

Aluno = {
    'nome': input('Nome: '),
    'idade': int(input('Idade: ')),
    'altura': float(input('Altura:')),
    'Contato': input('Seu contato:')
}


os.system('cls')
print(Aluno)
print ("""Soma: +
Subtração: - 
Multiplicação: *
Divisão: /
Média: %
Dobre o valor: ^ 
Converter minutos para segundos: M\n""")

metodo = input('Informe pelo simbolo ação que quer fazer: ')

if metodo != '%' and metodo != '^':
    x = float(input('Primeiro valor: '))
    y = float(input('Segundo valor: '))
    if metodo == '/':
        print('O valor da divisão é: {:.2f}'.format(div(x, y)))
    if metodo == '*':
        print('O valor da multiplicação é: {:.2f}'.format(mult(x,y)))
    if metodo == '-':
        print('O valor da subtração: {:.2f}'.format(sub(x,y)))
    if metodo == '+':
        print('O valor da soma: {:.2f}'.format(soma(x,y)))
elif metodo == '^':
    x = float(input('Informe o valor: '))
    print('O dobro de {0:.2f} é {1:.2f}'.format(x, x*2))
elif metodo == '%':
    x = float(input('Primeiro valor: '))
    y = float(input('Segundo valor: '))
    z = float(input('Terceiro valor: '))
    print('A média é: {}'.format(med(x,y,z)))
if metodo == 'M':
    x = int(input('Informe o minuto/s: '))
    print('{0} minuto/s em segnudos é: {1}'.format(x, x*60))

