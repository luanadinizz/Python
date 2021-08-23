n=int(input('digite a dimensao da matriz quadrada:'))
m = []
max = None
position = (0, 0)
min=None
position = (0, 0)
for i in range(n):
 linha = []
 for j in range(n):
 value = int(input("Valor da posição ({}, {}):".format(i, j)))
 if max is None or value > max:
 max = value
 positionm = (i, j)
 linha.append(value)
 if min is None or value< min:
 min=value
 position=(i,j)
 linha.append(value)
 m.append(linha)
print("O maior valor está na posição {} e vale {}".format(positionm, max))
print("O menor valor está na posição {} e vale {}".format(position, min))
