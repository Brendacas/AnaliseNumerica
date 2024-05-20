from sympy import *
import math
import numpy as np


def processar_arquivo_entradas():
  arq = open("entradas.txt", "r")
  valX = []
  valY = []

  linha = None
  while (linha != ''):
    linha = arq.readline()
    if (linha != ""):
      aux = linha.split(";")
      x_aux = aux[0].split(",")
      y_aux = aux[1].split("\n")
      y_aux = y_aux[0].split(",")

      for i in range(len(x_aux)):
        x_aux[i] = eval(x_aux[i])

      for i in range(len(y_aux)):
        y_aux[i] = eval(y_aux[i])

      dick = {}
      for i in range(len(x_aux)):
        dick[x_aux[i]] = y_aux[i]

      valX.append(x_aux)
      valY.append(dick)

  arq.close()

  return valX, valY


def interpNewton(valX, valY):
  n = len(valX)
  if (n == 1):
    return valY[valX[0]]
  if (n == 2):
    return (valY[valX[0]] - valY[valX[1]]) / (valX[0] - valX[1])
  else:
    return (interpNewton(valX[0:n - 1], valY) -
            interpNewton(valX[1:n], valY)) / (valX[0] - valX[n - 1])


def newton(valX, valY):
  x = Symbol("x")
  resultado = 0
  variaveis = 1
  n = len(valX)
  aux = []
  for i in range(n):
    aux.append(valX[i])
    resultado += variaveis * round(interpNewton(aux, valY), 2)
    variaveis *= Poly(x - valX[i])
  return str(resultado.args[0])


def main():
  x, y = processar_arquivo_entradas()
  arq = open("saidas.txt", "w")
  for i in range(len(x)):
    resultado = newton(x[i], y[i])
    arq.write("f(x) = " + str(resultado))
    if (i < len(x) - 1):
      arq.write("\n")
  arq.close()


main()
