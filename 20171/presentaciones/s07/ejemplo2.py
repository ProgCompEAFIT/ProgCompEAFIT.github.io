import random
import ejemplo1

def cll(n,m,li,ls):
    megalist = []
    for i in range(n):
        megalist.append(ejemplo1.createRandomList(m,li,ls))
    return megalist





























#print(cll(10,10,0,5))

#n = int(raw_input("ingrese cantidad elementos:"))
#lim_inf = int(raw_input("ingrese limite inferior:"))
#lim_sup = int(raw_input("ingrese limite superior:"))

#print(createRandomList(n,lim_inf,lim_sup))
