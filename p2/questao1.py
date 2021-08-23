def duracao():
 horainicio=hi*60
 mininicio=mi
 horafim=hf*60
 minfim=mf
 tempo=(horafim+minfim)-(horainicio+mininicio)
 print('a duracao foi de', tempo, 'minutos')
print('horario do inicio:')
hi=int(input('digite a hora:'))
mi=int(input('digite os minutos:'))
print('horario do fim:')
hf=int(input('digite a hora:'))
mf=int(input('digite os minutos:'))
duracao()
