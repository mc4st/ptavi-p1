#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys

def main():
    pass
def suma(sum1, sum2):
    return sum1 + sum2
def multiplicación(ope1, ope2):
    return ope1*ope2
if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[2]) # ya que nos muestra una lista con cadenas de        caracteres y la tenemos que pasar a int
        operando2 = int(sys.argv[3])
    execpt ValueError:
        sys.exit('¡Deben ser números enteros!')
    print(suma(operando1,operando2))
    print(multiplicacion(operando1,operando2))
