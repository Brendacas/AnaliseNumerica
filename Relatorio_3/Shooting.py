import math
from sympy import *

def processar_arquivo_entradas():
    arq = open("entrada.txt", "r")
    x = symbols('x')

    funcao = []
    y_inicial = []
    intervalo = []
    valor = []
    h = []
    n = []

    linha = None
    while (linha != ''):
        linha = arq.readline()
        if (linha != ""):
            aux = linha.split(";")
            funcao_aux = eval(aux[0])

            y_inicial_aux = eval(aux[1])

            intervalo_aux = aux[2]
            intervalo_aux = intervalo_aux.split(",")
            for i in range (len(intervalo_aux)):
                intervalo_aux[i] = eval(intervalo_aux[i])

            valor_aux = eval(aux[3])

            h_aux = eval(aux[4])

            n_aux = aux[5]
            n_aux = n_aux.split("\n")
            n_aux = eval(n_aux[0])

            funcao.append(funcao_aux)
            y_inicial.append(y_inicial_aux)
            intervalo.append(intervalo_aux)
            valor.append(valor_aux)
            h.append(h_aux)
            n.append(n_aux)
    arq.close()

    return funcao, y_inicial, intervalo, valor, h, n

def shooting(funcao, y_inicial, intervalo, valor, h, pontos):
    x = symbols('x')

    y_final = []

    x_y_z = [[], [], []]

    for j in range(len(x_y_z)):
        x_y_z[0] = [0]
        x_y_z[1] = [y_inicial]
        if j != 2:
            x_y_z[2] = [intervalo[j]]
            for i in range(pontos):        
                x_y_z[1].append(x_y_z[1][i] + h *x_y_z[2][i])
                x_y_z[2].append(x_y_z[2][i] + h * funcao.subs(x, x_y_z[0][i]))
                x_y_z[0].append(x_y_z[0][i] + h)
            y_final.append(x_y_z[1][-1])
        else:
            x_y_z[2] = [intervalo[0] + ( (intervalo[1]-intervalo[0]) / (y_final[1]-y_final[0]) ) * (valor-y_final[0])]
            for i in range(pontos):
                x_y_z[1].append(x_y_z[1][i] + h * x_y_z[2][i])
                x_y_z[2].append(x_y_z[2][i] + h * funcao.subs(x, x_y_z[0][i]))
                x_y_z[0].append(x_y_z[0][i] + h)

        if x_y_z[1][-1] == valor: 
            resultado = []
            for i in range (len(x_y_z[1])):
                resultado.append([i, round(x_y_z[1][i], 3)])

            return resultado

def main():
    funcao, y_inicial, intervalo, valor, h, n = processar_arquivo_entradas()
    arq = open("saidas.txt", "w")
    for i in range (len(funcao)):
        resultado = shooting(funcao[i], y_inicial[i], intervalo[i], valor[i], h[i], n[i])
        arq.write(str(resultado))
        if (i < len(funcao)-1):
            arq.write("\n")
    arq.close()

main()