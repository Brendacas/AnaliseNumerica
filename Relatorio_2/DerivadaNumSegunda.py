from sympy import *
import numpy as np
import math


def processar_arquivo_Entradas():
  arq = open("entrada.txt", "r")
  x = Symbol("x")
  f = []
  valor_x = []

  linha = None
  while (linha != ''):
    linha = arq.readline()
    if (linha != ""):
      aux = linha.split(";")
      f_aux = eval(aux[0])

      x_aux = aux[1].split("\n")
      x_aux = eval(x_aux[0])

      f.append(f_aux)
      valor_x.append(x_aux)

  arq.close()

  return f, valor_x


def derivadaNumSegunda(f, valor_x):
  x = Symbol("x")

  segunda_derivada = (
      (f.subs(x, str(float(valor_x) + 1)) - f.subs(x, valor_x)) -
      f.subs(x, valor_x) - f.subs(x, str(float(valor_x) - 1)))

  return round(segunda_derivada, 4)


def main():
  f, valor_x = processar_arquivo_Entradas()
  arq = open("saidas.txt", "w")
  for i in range(len(f)):
    resultado = derivadaNumSegunda(f[i], valor_x[i])
    arq.write("Derivação = " + str(resultado))
    if (i < len(f) - 1):
      arq.write("\n")
  arq.close()


main()
