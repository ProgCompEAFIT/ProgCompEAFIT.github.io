import random

midict = {"B":range(1,16),"I":range(16,31),"N":range(31,46),"G":range(46,61),"O":range(61,76)}



#print sorted(midict.keys())


def tarjeta(midict):
    la_tarjeta = {}
    la_tarjeta["B"] = sorted(random.sample(midict["B"],5))
    la_tarjeta["I"] = sorted(random.sample(midict["I"],5))
    la_tarjeta["N"] = sorted(random.sample(midict["N"],5))
    la_tarjeta["G"] = sorted(random.sample(midict["G"],5))
    la_tarjeta["O"] = sorted(random.sample(midict["O"],5))
    return la_tarjeta

def imp_tarjeta(una_tarjeta):
    #resultado = " %s\t%s\t%s\t%s\t%s\n" % ("B", "I", "N", "G", "O")
    resultado = " B\tI\tN\tG\tO\n"
    for i in range(5):
        resultado += " %s\t%s\t%s\t%s\t%s\n" % (una_tarjeta["B"][i],una_tarjeta["I"][i],una_tarjeta["N"][i],una_tarjeta["G"][i],una_tarjeta["O"][i])
    return resultado

entrada = raw_input("ingrese los argumentos del programa")
#entrada = "Bingo.py llamados.txt t1.txt t2.txt t3.txt"
entrada = entrada.split()



a = tarjeta(midict)

print imp_tarjeta(a)
#print a
