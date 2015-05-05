#!/usr/bin/python

import sys


def sumar(operando1, operando2):
    print operando1 + operando2


def restar(operando1, operando2):
    print operando1 - operando2


def multiplicar(operando1, operando2):
    print operando1 * operando2


def dividir(operando1, operando2):
    try:
        print (operando1) / (operando2)
    except ZeroDivisionError:
    	sys.exit("Imposible dividir entre 0")

if __name__ == "__main__":
    try:
    	operando1 = float(sys.argv[2])
    	operando2 = float(sys.argv[3])
    	if sys.argv[1] == "sumar":
    		sumar(operando1, operando2)
    	elif sys.argv[1] == "restar":
    		restar(operando1, operando2)
    	elif sys.argv[1] == "multiplicar":
    		multiplicar(operando1, operando2)
    	elif sys.argv[1] == "dividir":
    		dividir(operando1, operando2)
    	else:
    		print "Uso: Operaciones disponibles: +  -  *  /"
    except ValueError:
    	sys.exit("Al menos uno de los operandos no es un numero")
    except IndexError:
    	sys.exit("Uso: python calculadora.py funcion operando1 operando2")
