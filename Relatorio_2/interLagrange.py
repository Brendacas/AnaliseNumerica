from sympy import *
import math


def processar_arquivo_entradas():
  arq = open("entrada.txt", "r")
  xp = []
  y = []

  linha = None
  while (linha != ''):
    linha = arq.readline()
    if (linha != ""):
      aux = linha.split(";")

      xp_aux = aux[0].split(",")
      for i in range(len(xp_aux)):
        xp_aux[i] = eval(xp_aux[i])

      y_aux = aux[1].split("\n")
      y_aux = y_aux[0].split(",")
      for i in range(len(y_aux)):
        y_aux[i] = eval(y_aux[i])

      xp.append(xp_aux)
      y.append(y_aux)

  arq.close()

  return xp, y


def interpLagrange(k, xp, n):
  x = Symbol("x")

  lagr = 1
  for i in range(n):
    if (i != k):
      lagr *= Poly((x - xp[i]) / (xp[k] - xp[i]))
  return lagr


def lagrange(xp, y):
  n = len(xp)

  resp = 0
  for i in range(n):
    resp += interpLagrange(i, xp, n) * y[i]

  resp = resp.args[0]
  return str(resp)


def main():
  xp, y = processar_arquivo_entradas()
  arq = open("saidas.txt", "w")
  for i in range(len(xp)):
    resultado = lagrange(xp[i], y[i])
    arq.write("f(x) = " + str(resultado))
    if (i < len(xp) - 1):
      arq.write("\n")
  arq.close()


main()
