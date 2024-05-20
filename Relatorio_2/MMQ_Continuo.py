from sympy import *
import math


def processar_arquivo_entradas():
  arq = open("entrada.txt", "r")
  x = Symbol('x')
  f = []
  intervalo = []

  linha = None
  while (linha != ''):
    linha = arq.readline()
    if (linha != ""):
      aux = linha.split(";")
      f_aux = eval(aux[0])

      aux_intervalo = aux[1].split("\n")
      aux_intervalo = aux_intervalo[0]
      aux_intervalo = aux_intervalo.split(",")

      for i in range(len(aux_intervalo)):
        aux_intervalo[i] = eval(aux_intervalo[i])

      f.append(f_aux)
      intervalo.append(aux_intervalo)

  arq.close()

  return f, intervalo


def mmq_Continuo(f, intervalo):
  x = Symbol("x")
  funcoes = [1, eval("x"), eval("x**2")]
  matrizAux = zeros(len(funcoes))
  vetor_F = zeros(len(funcoes), 1)

  contador = 0
  for i in range(len(funcoes)):
    aux = funcoes[i] * f
    vetor_F[i, 0] = integrate(aux, (x, (intervalo[0], intervalo[1])))
    for j in range(len(funcoes)):
      aux = funcoes[i] * funcoes[j]
      matrizAux[i, j] = aux

      contador += 1
      if (contador == len(funcoes)):
        for contador in range(len(funcoes)):
          matrizAux[i, contador] = integrate(matrizAux[i, contador],
                                             (x, (intervalo[0], intervalo[1])))
        contador = 0

  resultado = matrizAux.LUsolve(vetor_F)

  potencializacao = 1
  result_final = 0
  for i in range(len(funcoes)):
    result_final += resultado[i, 0] * potencializacao
    potencializacao *= x

  return result_final


def main():
  f, intervalo = processar_arquivo_entradas()
  arq = open("saidas.txt", "w")
  for i in range(len(f)):
    resultado = mmq_Continuo(f[i], intervalo[i])
    arq.write("f(x) = " + str(resultado))
    if (i < len(f) - 1):
      arq.write("\n")
  arq.close()


main()
