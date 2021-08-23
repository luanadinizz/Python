frase=str(input(‘digite uma frase:’)).strip().upper()
palavras=frase.split()
junto=’ ‘.join(palavras)
inverso=’’
for letra in range (len(junto)-1, -1,-1):
	inverso=inverso+junto[letra]
if inverso==junto:
	print(‘e um palindromo’)
else:
	print(‘não e um palindromo’)
