minutos = float(input('Minutos: '))
sobra = minutos%60
horas = (minutos-sobra)/60
print(f'Sao: {horas:.0f}h{sobra:.0f}')