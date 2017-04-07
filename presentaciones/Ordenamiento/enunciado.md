
# Actividad: Comparación entre Ordenamientos

## Descripción:

Crear un programa que nos permita hacer una análisis de complejidad a través del tiempo que toma un algoritmo determinado en ordenar una lista de un tamaño determinado.

+ Crear para el Ordenamiento Burbuja(Bubble)
+ Crear para el ordenamiento rápido (Quicksor)


# Preguntas

## Que hace la función timeit de la biblioteca timeit

## si se varia el tamaño de las listas aleatorias que comportamiento se tiene

+ 10 elementos
+ 100 elementos
+ 1000 elementos
+ 10000 elementos
+ 1000000 elementos


# Ejemplo

+ [crear lista aleatoria de tamaño 'n' ](lista.py)

```python
import random

tam = 100
lista  = random.sample(range(0,tam+1),tam)
print lista

```


+ [algoritmo de ordenamiento por inserción](insort.py)



```python
import random

def insertionSort():
    tam = 100
    lista  = random.sample(range(0,tam+1),tam/4)
    print lista
    for index in range(1,len(lista)):

        actual = lista[index]
        pos = index

        while pos>0 and lista[pos-1]>actual:
            lista[pos]=lista[pos-1]
            pos = pos-1

        lista[pos]=actual
    print lista

for i in range(3): insertionSort()

```

+ [ejemplo análisis complejidad](sol2.py)


```python
import random

def insertionSort():

    tam = 100000
    lista  = random.sample(range(0,tam+1),tam)
    print lista
    for index in range(1,len(lista)):

        actual = lista[index]
        pos = index

        while pos>0 and lista[pos-1]>actual:
            lista[pos]=lista[pos-1]
            pos = pos-1

        lista[pos]=actual
    print lista

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("insertionSort()", setup="from __main__ import insertionSort", number=1))

```
