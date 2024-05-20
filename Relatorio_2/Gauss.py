from sympy import *
import math

def abrirEntradas():
    arq = open("entradas.txt", "r")
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

def gauss(f, intervalo, n):
    x = Symbol("x")
    h = (intervalo[1] - intervalo[0])/n
    x_aux = intervalos(intervalo[0], intervalo[1], h)

    resultado = 0
    for i in range(n):
        alpha = (x_aux[i+1] - x_aux[i])/2
        beta = (x_aux[i+1] + x_aux[i])/2 
        x1 = alpha * -math.sqrt(3/5) + beta
        x2 = beta
        x3 = alpha * math.sqrt(3/5) + beta

        quadratura_gauss = (5/9 * f.subs(x, x1) + 8/9 * f.subs(x, x2) + 5/9 * f.subs(x, x3)) * h/2
        resultado = resultado + quadratura_gauss
    return round(resultado, 2)

def main():
  f, intervalo, subs = processar_arquivo_entradas()
  arq = open("saidas.txt", "w")
  for i in range (len(f)):
    resultado = gauss(f[i], intervalo[i], subs[i])
    arq.write("Integração = " + str(resultado))
    if (i < len(f)-1):
      arq.write("\n")
  arq.close()

main()