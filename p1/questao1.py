valor=int(input('digite um valor:'))
total=valor
ced=100
totalced=0
while True:
  if total>=ced:
     total=total-ced
     totalced=totalced+1
  else:
    print(f'total de {totalced} cédulas de R$ {ced}')
    if ced==100:
      ced=50
    elif ced==50:
      ced=20
    elif ced==20:
      ced=10
    elif ced==10:
      ced=5
    elif ced==5:
      ced=2
    elif ced==2:
      ced=1
    totalced=0
    if total==0:
      break
