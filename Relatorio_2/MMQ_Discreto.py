from sympy import *
import math
import numpy as np

def processar_arquivo_entradas():
    arq = open("entrada.txt", "r")
    x = Symbol("x")
    valor_x = []
    valor_y = []

    linha = None
    while (linha != ''):
        linha = arq.readline()
        if (linha != ""):
            aux = linha.split(";")
            x_aux = aux[0]
            x_aux = x_aux.split(",")

            for i in range (len(x_aux)):
                x_aux[i] = eval(x_aux[i])

            f = aux[1].split("\n")
            f = f[0]
            f = f.split(",")

            for i in range (len(f)):
                f[i] = eval(f[i])

            valor_x.append(x_aux)
            valor_y.append(f)

    arq.close()

    return valor_x, valor_y

def mmqDiscreto(sX, f):
    x = Symbol("x")
    funcao = [1, eval("x"), eval("x**2")]
    tamFuncao = len(funcao)
    tam_X = len(sX)
    matrizUi = [tam_X*[1]]

    listaAux = []
    for i in range(tamFuncao):
        aux = funcao[i]
        if(aux != 1):
            for elem in sX:
                listaAux.append(aux.subs(x, elem))

            matrizUi.append(listaAux)
            listaAux = []

    vetor_F = zeros(tamFuncao, 1)
    matrizResult = zeros(tamFuncao)
    for i in range(tamFuncao):
        for j in range(tamFuncao):
            matrizResult[i,j] = sum(np.multiply(matrizUi[i], matrizUi[j]))
        vetor_F[i] = sum(np.multiply(f, matrizUi[i]))
    resultado = matrizResult.LUsolve(vetor_F)

    potencializacao = 1
    result_final = 0
    for i in range(tamFuncao):
        result_final += round(resultado[i,0], 2) * potencializacao
        potencializacao *= x

    return result_final

def main():
    x, f = processar_arquivo_entradas()
    arq = open("saidas.txt", "w")
    for i in range (len(x)):
        resultado = mmqDiscreto(x[i], f[i])
        arq.write("f(x) = " + str(resultado))
        if (i < len(x)-1):
            arq.write("\n")
    arq.close()
main()