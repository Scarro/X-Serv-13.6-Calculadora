#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Sergio Carro Albarrán
# Calculadora simple en python

import sys


def sumar(operando1, operando2):
	return operando1 + operando2


def restar(operando1, operando2):
	return operando1 - operando2


def multiplicar(operando1, operando2):
	return operando1 * operando2


def dividir(operando1, operando2):
	return operando1 / operando2


if __name__ == "__main__":
	try:
		if len(sys.argv) != 4:
			raise IndexError(len(sys.argv)-1)
		funcion = str(sys.argv[1])
		operando1 = float(sys.argv[2])
		operando2 = float(sys.argv[3])
		print locals()[funcion](operando1, operando2)
	except ValueError:
		sys.exit("Al menos uno de los operandos no es un número")
	except IndexError as e:
		mensaje = "Uso: python calculadora.py funcion operando1 operando2"
		sys.exit('(' + str(e.args[0]) + ') ' + mensaje)
	except KeyError as e:
		print(str(e.args[0]) + " no es una función permitida")
		sys.exit("Operaciones: sumar, restar, multiplicar, dividir")
	except ZeroDivisionError:
		sys.exit("Imposible dividir entre 0")
		