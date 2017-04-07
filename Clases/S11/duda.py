import random

#l = random.sample(range(0,1000),15)
l = [349, 99, 49, 786, 52, 356, 207, 865, 271, 569, 213, 99, 282, 880, 247]

print l

elemento = 999

pos = []
for i in range(0,len(l)):
    if(l[i]==elemento): pos.append(i)

if(len(pos)>0): print ("hemos encontrado el elemento en: {}").format(pos)
else: print("no hemos encontrado el elemento buscado: {}").format(elemento)
