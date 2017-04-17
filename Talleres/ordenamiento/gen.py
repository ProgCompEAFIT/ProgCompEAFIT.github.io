import random

cases = random.randint(0,6) # casos

def printlista(lista):
    print(len(lista))
    s = ""
    for i in lista:
        s+=str(i)+" "
    print s

for c in range(cases):
    lista = []
    players = random.randint(1,15) # jugadores
    for p in range(players):
        lista.append(random.randint(0,100000))
    printlista(lista)
