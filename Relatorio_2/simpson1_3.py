from sympy import *
import sympy as sp
import math

def processar_arquivo_Entradas():
    arq = open("entrada.txt", "r")
    x = Symbol("x")
    f = []
    intervalo = []
    subs = []

    linha = None
    while (linha != ''):
        linha = arq.readline()
        if (linha != ""):
            aux = linha.split(";")
            f_aux = eval(aux[0])

            intervalo_aux = aux[1]
            intervalo_aux = intervalo_aux.split(",")

            for i in range (len(intervalo_aux)):
                intervalo_aux[i] = eval(intervalo_aux[i])

            sub_aux = aux[2]
            sub_aux = sub_aux.split("\n")
            sub_aux = eval(sub_aux[0])

            f.append(f_aux)
            intervalo.append(intervalo_aux)
            subs.append(sub_aux)

    arq.close()

    return f, intervalo, subs

def intervalos(inicio, final, h):
  x_aux = [inicio]
  aux = inicio + h
  while(aux < final):
    x_aux.append(aux)
    aux += h
  x_aux.append(aux)
  return x_aux

def simpson1_3(f, intervalo, n):
  x = Symbol("x")
  h = (intervalo[1] - intervalo[0]) / (2 * n)
  x_aux = intervalos(intervalo[0], intervalo[1], h)
  tamanho = len(x_aux)

  resultado = f.subs(x, intervalo[0]) + f.subs(x, intervalo[1])
  for i in range(1, tamanho-1):
    aux = f.subs(x, x_aux[i])
    if(i%2 == 0):
      resultado += 2*aux
    else:
      resultado += 4*aux
  resultado *= h/3

  return round(resultado, 2)


def main():
  f, intervalo, subs = processar_arquivo_Entradas()
  arq = open("saidas.txt", "w")
  for i in range (len(f)):
    resultado = simpson1_3(f[i], intervalo[i], subs[i])
    arq.write("Integração = " + str(resultado))
    if (i < len(f)-1):
      arq.write("\n")
  arq.close()

main()
