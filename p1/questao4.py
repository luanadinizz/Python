import math
sum=0
x=int(input('digite um angulo:'))
for n in range(20):
 sum+= math.pow(-1,n)/math.factorial(2*n+1)*math.pow(x,2*n+1)
print(f'o seno do angulo vale:{sum}')
