#Estrutura for#
print("******Estrutura for******")
for i in range(1, 20+1):
  if (i == 13):
    continue
  print(i,"º Andar")

 #Estrutura while#
print("******Estrutura while******")
i=0
while (i<=20-1):
  i+=1
  if i==13:
    continue
  print(i,"º Andar")

#Estrutura for - DESAFIO DECRESCENTE#
print("******Estrutura for DESAFIO DECRESCENTE******")
for i in range(20, 0, -1):
  if (i == 13):
    continue
  print(i,"º Andar")

 #Estrutura while - DESAFIO DECRESCENTE#
print("******Estrutura while DESAFIO DECRESCENTE******")
i=21
while (i>1):
  i-=1
  if i==13:
    continue
  print(i,"º Andar")



