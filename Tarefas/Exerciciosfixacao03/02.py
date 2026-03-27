nota = float(input('Nota: '))

if nota < 5:
    print('Rodou, faz dnv')
elif nota < 6.9:
    print('Recuperação')
elif nota < 8.9:
    print('Aprovada(o)')
else:
    print('Aprovada(o) com exelencia')