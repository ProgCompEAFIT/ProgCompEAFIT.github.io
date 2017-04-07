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
