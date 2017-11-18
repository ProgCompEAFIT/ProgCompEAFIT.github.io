# EVALUACIÓN FINAL 2017-2
# PROGRAMACIÓN DE COMPUTADORES(ST0240)
# FUNDAMENTOS DE PROGRAMACIÓN (ST0286)

## Instrucciones Iniciales

Bienvenido a la evaluación final de las materias ST0240 y ST0286,

## Compromiso de Integridad

Durante el examen se pasará firmando la asistencia al mismo. Al firmar usted está aceptando que se encuentra de acuerdo con las políticas del examen dadas a continuación:

* Usted se encuentra sentado en una silla específica, al firmar debe poner el número marcado con cinta verde en la esquina superior de la pantalla.


* No puede hacer uso de dispositivos diferentes al computador de la universidad.
al firmar debe poner el número asignado.


De acuerdo con lo estipulado en el comunicado el uso de dispositivos diferentes a los permitidos es considerado fraude y el **único** dispositivo permitido es el pc de la universidad.


Hay 10 tipos de examenes diferentes, para saber cuál es su tema mire el último dígito que tiene asignado su puesto, sus respuestas deberán corresponder a dicho dígito.


## Enunciado

La red sísmica del Servicio Geológico Colombiano le entrega los siguientes datos
pertenecientes al año 2015 y le otorga las siguientes tareas:

### De los siguientes puntos escoja 3:


1.

2. Entregue un diccionario con el código y magnitud de los 5 mayores sismos para el mes asignado

3. Gráficar  en un diagrama de barras (histograma) con la profundiad promedio de mes asignado

4. Gráficar en un diagrama de barras (histograma) de cantidad de sismos por día
para el mes asignado.


### Datos de Entrada:

[Descargar](https://www.datos.gov.co/api/views/c6z5-qfp4/rows.csv?accessType=DOWNLOAD)

### Salida Esperada:

## ENTREGA

La evaluación del final será comparando las respuestas dadas con las respuestas esperadas, para que sus respuestas sean validas debe adjuntar el código con el que las generó de lo contrario sus respuestas **NO SERAN TENIDAS EN CUENTA**


## AYUDAS


```python
# -*- coding: utf-8 -*-
import datetime
import timedelta

class Sismo:

    def __init__(self, fecha,departamento,municipio):
        self.fecha = fecha
        self.departamento = departamento
        self.municipio = municipio

def to_date(fecha_str,hora_str):
    #recibe string, retorna un datetime
    d = [int(x) for x in fecha_str.split()[0].split('/')]
    t = [int(x) for x in hora_str.split(':')]
    return datetime.datetime(d[2],d[0],d[1],*t)

```
