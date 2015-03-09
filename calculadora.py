#!/usr/bin/python
import sys


def sumar(val1, val2):
	print float(val1) + int(val2)

def restar(val1, val2):
	print float(val1) - int(val2)

def multiplicar(val1, val2):
	print float(val1) * int(val2)

def dividir(val1, val2):
	print float(val1) / int(val2)

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
		print("Al menos uno de los 2 numeros es incorrecto")
	except IndexError:
		print("Falta al menos un numero por introducir")
	except ZeroDivisionError:
		print("Imposible dividir entre 0")