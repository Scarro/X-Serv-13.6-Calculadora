"""
Script para crear una calculadora simple

Ejecucion:
$python calculadora.py Operacion operador1 operador2
"""

#!/usr/bin/python

import sys
import os

funciones = ['suma','resta','multiplicacion','division']

def sumar(val1, val2):
    print(val1 + val2)
def restar(val1, val2):
    print(val1 - val2)
def multiplicar(val1, val2):
    print(val1 * val2)
def dividir(val1, val2):
    try:
        print (float(val1) / float(val2))
    except ZeroDivisionError:
        print "Imposible dividir entre 0"

if len(sys.argv != 4):
    sys.exit("Uso: $ python calculadora.py Operacion operador1 operador2")

if __name__ == "__main__":
    try:
        if sys.argv[1] == "Sumar":
            sumar(sys.argv[2],sys.argv[3])
        if sys.argv[1] == "Restar":
            restar(sys.argv[2],sys.argv[3])
        if sys.argv[1] == "Multiplicar":
            multiplicar(sys.argv[2],sys.argv[3])
        if sys.argv[1] == "Dividir":
            dividir(sys.argv[2],sys.argv[3])
    except ValueError:
        print("Al menos uno de los dos numeros es incorrecto")
    except IndexError:
        print("Falta al menos un numero por introducir")
