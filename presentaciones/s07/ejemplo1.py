import random

def createRandomList(n,li,ls):
    a = []
    for i in range(n):
        a.append(random.randint(li,ls))
    return a




























#print(createRandomList(10,0,5))
#print(createRandomList(100,0,50))
#print(createRandomList(1000,0,500))

#n = int(raw_input("ingrese cantidad elementos:"))
#lim_inf = int(raw_input("ingrese limite inferior:"))
#lim_sup = int(raw_input("ingrese limite superior:"))

#print(createRandomList(n,lim_inf,lim_sup))
