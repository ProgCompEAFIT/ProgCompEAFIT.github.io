import sys

print "Se muestra siempre en Ej1"

if __name__ == "__main__":
    print "Se muestra si no es importacion estoy en Ej1"
    print __name__

def readfile():

    resultado = "Lectura Exitosa!"

    try:
        nombrearchivo = sys.argv[1]
    except IndexError:
        resultado = "No ingreso el nombre de entrada "


    try:
        archivo = open(nombrearchivo,'r')
        for i in range(10):
            print(archivo.readline().rstrip())
    except IOError:
        resultado = "nombre de archivo incorrecto"

    return resultado
