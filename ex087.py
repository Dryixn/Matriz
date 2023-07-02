matriz = []
terceira = []
segunda = []

print('=' * 80)
for m in range(1, 10):
    matriz.append(int(input(f'{m}º número da matriz: ')))
print('=' * 80)

for v in range(0, 3):
    print(f'[ {matriz[v]} ] ', end = '')
    if matriz[v] == matriz[2]:
        terceira.append(matriz[v])
print()

for b in range(3, 6):
    print(f'[ {matriz[b]} ] ', end = '')
    if matriz[b] == matriz[5]:
        terceira.append(matriz[b])
    segunda.append(matriz[b])
print()

for n in range(6, 9):
    print(f'[ {matriz[n]} ] ', end = '')
    if matriz[n] == matriz[8]:
        terceira.append(matriz[n])
print()
print('=' * 80)

print(f'A soma de todos os valores é {sum(matriz)}.')
print(f'A soma dos valores daterceira coluna é {sum(terceira)}.')
print(f'O maior valor da segunda linha é {max(segunda)}.')
print('=' * 80)
