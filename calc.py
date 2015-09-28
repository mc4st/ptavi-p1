#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys

def main():
    pass
def suma(sum1, sum2):
    return sum1 + sum2
def resta(sum1, sum2):
    return sum1 - sum2
def multiplicacion(ope1, ope2):
    return ope1*ope2
def division(ope1, ope2):
    return ope1/ope2
if __name__ == "__main__":
    try:
        operando1 = float(sys.argv[1]) # ya que nos muestra una lista con cadenas de        caracteres y la tenemos que pasar a int
        operando2 = float(sys.argv[3])
        operacion = sys.argv[2]
    except ValueError:
        sys.exit('¡Deben ser números enteros!')
    if operacion == 'suma':
        print(suma(operando1,operando2))
    elif operacion == 'resta':
        print(resta(operando1,operando2))
    elif operacion == 'multiplicacion':
        print(multiplicacion(operando1,operando2))
    elif operacion == 'division':
        if operando2 != 0:
            print(division(operando1,operando2))
        else:
            sys.exit('¡Indeterminación!')
