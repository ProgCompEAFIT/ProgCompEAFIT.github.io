# Programación de Computadores

Hola, bienvenido a la página NO oficial de Programación de computadores de la _Universidad EAFIT_

## 1. [Programa de la materia](https://drive.google.com/open?id=0B0tZOopbjoslRHEzc1luZDZQZlE)



## 2. [Profesores](profesores/profes.md)

## [Monitores](monitores.md)

## Presentaciones

  + [Semana 8: Ordenamiento y Búsqueda](presentaciones/s8.md)
  + [Semana 7](presentaciones/s7.md)


## Ejemplos
 + Semana 8:
    + [Ejemplo 1](2.Ejercicios/Semana8/Ejemplo1.md)
    + [Bubble Sort]()

    ```python
    def bubbleSort(alist):
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i]>alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp

    alist = [54,26,93,17,77,31,44,55,20]
    bubbleSort(alist)
    print(alist)
    ```


## Ejercicios
  - Semana 8

## Recursos Adicionales

1. [Libro: A Byte of Python](https://python.swaroopch.com/)
1. [Libro: Python para todos](https://launchpadlibrarian.net/18980633/Python%20para%20todos.pdf)
