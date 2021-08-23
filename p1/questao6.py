N=int(input('digite a quantidade total de azulejos brancos:'))
soma=0
A=int(input('digite um numero:'))
B=int(input('digite outro numero:'))
for i in range(1,N):
 if i%A==0 or i%B==0:
 soma=soma+1
print(f'o total de azulejos sera de {soma}')
