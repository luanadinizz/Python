media = 0
soma = 0
mm = 0
maiormedia = 0
menormedia = 0
manha = 0
tarde = 0
for p in range(1, 101):
 print('----',p,'maquina ----')
 codigo = str(input('digite o codigo da maquina:'))
 torneiro = str(input('digite o nome do torneiro:'))
 largura = float(input('digite a largura da peca:'))
 comprimento = float(input('digite o comprimento da peca:'))
 expessura = float(input('digite a expessura da peca:'))
 data=str(input('insira a data de fabricacao:'))
 turno = int(input('digite em que turno a peca foi fabricada:1-manha,2-tarde'))
 media = (largura + comprimento + expessura) / 3
 soma = soma + media
 if media<=11.48:
 print('a peca feita pelo torneiro', torneiro, 'obteve a media', media, 'e foi rejeitada')
 if media>11.48 and media<11.51:
 print('a peca feita pelo torneiro', torneiro, 'obteve a media', media, 'e foi aprovada')
 if media>=11.51:
 print('a peca feita pelo torneiro', torneiro, 'obteve a media', media, 'e foi reaproveitada')
 if p == 1:
 maiormedia = menormedia = media
 if media > maiormedia:
 maiormedia = media
 if turno == 1:
 manha = manha + 1
 if turno == 2:
 tarde = tarde + 1
mm=media/100
print('a media das medias foi:',mm)
print('a maior media foi:',maiormedia)
print('a menor media foi:',menormedia)
print('o total de pecas construidas no periodo da manha foi de:',manha,'e no periodo da tarde foi de :', tarde)
