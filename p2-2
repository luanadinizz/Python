nome=input('digite o nome do arquivo que contem o nome dos alunos:')
arqnome=open(nome,"r")
notas=input('digite o nome do arquivo que contem as notas dos alunos:')
arqnotas=open(notas,"r")
media=open('mediafinal.txt',"w")
lista=[]
for nome1l,notas1l in zip(nome,notas):
 nome1l=nome1l.strip().split('')
 notas1l=notas1l.strip().split('')
 nome,notas=str(nome1l[0]),float(notas1l[0])
 lista.append([nome,notas])
 media.write((nome,notas))
 if notas1l>=6:
 print('aluno aprovado')
 if notas1l<6 and notas1l>=4:
 print('aluno em vs')
 if notas1l<4:
 print('aluno reprovado')
arqnome.close()
arqnotas.close()
media.close()
