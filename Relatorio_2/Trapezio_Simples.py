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

def trapezio_Simples(fx, intervalo, n):
    x = sp.Symbol("x")
    h = (intervalo[1] - intervalo[0]) / n
    x_aux = intervalos(intervalo[0], intervalo[1], h)


    resultado = 0
    for i in range(n):
        soma_trap = (1 / 2 * fx.subs(x, x_aux[i]) + 1 / 2 * fx.subs(x, x_aux[i + 1])) * h
        resultado =+ soma_trap

    return round(resultado, 2)

def main():
  f, intervalo, subs = processar_arquivo_Entradas()
  arq = open("saidas.txt", "w")
  for i in range (len(f)):
    resultado = trapezio_Simples(f[i], intervalo[i], subs[i])
    arq.write("Integração = " + str(resultado))
    if (i < len(f)-1):
      arq.write("\n")
  arq.close()

main()
