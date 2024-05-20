# importação das bibliotecas
import math
import numpy as np
import sympy as sp


# função para abrir o arquivo de entradas
def processar_arquivo_entrada():
  arq = open("entrada.txt", "r")
  valor_x = []
  valor_y = []

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

      valor_x.append(x_aux)
      valor_y.append(y_aux)

  arq.close()

  return valor_x, valor_y


# função para realizar a regressão linear
def regressao_linear(valor_x, valor_y):
  x = y = x_y = x_2 = 0
  tam = len(valor_x)

  x = sum(valor_x)
  y = sum(valor_y)
  for i in range(tam):
    x_y += valor_x[i] * valor_y[i]
    x_2 += valor_x[i]**2

  b = (tam * x_y - x * y) / (tam * x_2 - x**2)
  a = (y - b * x) / tam

  b = round(b, 2)
  a = round(a, 2)

  # retorna a equação da regressão linear
  if a > 0:
    return str(b) + "*x" + " + " + str(a)
  else:
    a *= -1
    return str(b) + "*x" + " - " + str(a)


def main():
  valor_x, valor_y = processar_arquivo_entrada()
  arq = open("saidas.txt", "w")
  # percorre os dados de entrada e realiza a regressão linear
  for i in range(len(valor_x)):
    resultado = regressao_linear(valor_x[i], valor_y[i])
    arq.write("y = " + str(resultado))
    if (i < len(valor_x) - 1):
      arq.write("\n")
  arq.close()


main()
