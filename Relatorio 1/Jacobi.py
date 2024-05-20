import numpy as np
import re

def gerarMatriz(f):
    matriz = []
    vetorB = []

    texto = f.readlines()
    tamSistema = len(texto) - 1

    for a in range(tamSistema):
        linha = [float(i.strip()) for i in re.findall("([\+ | \-]*[0-9]+[\.]*[0-9]*)", texto[a])]
        matriz.append(linha)

    return matriz, vetorB

def printMatriz(matriz):
    for i in matriz:
        print(i)
    print("\n")

def metodoJacobi(matriz, vetorB, precisao, maxIteracoes):
    vetorX = np.zeros(len(vetorB))
    vetorX_ant = np.zeros(len(vetorB))

    # Itera até a convergência ou atingir o número máximo de iterações
    for iteracao in range(maxIteracoes):
        # Calcula o novo vetor solução
        for i in range(len(matriz)):
            if i < len(vetorB):
                soma = 0
                for j in range(i):
                    soma += matriz[i][j] * vetorX[j]
                vetorX[i] = (vetorB[i] - soma) / matriz[i][i]

        # Verifica se a convergência foi atingida
        erro = np.linalg.norm(vetorX - vetorX_ant)
        vetorX_ant = vetorX
        if erro < precisao:
            break

    return vetorX


def main():
    # Abre o arquivo de entrada
    f = open("entrada.txt", "r")

    # Gera a matriz e o vetor de entrada
    matriz, vetorB = gerarMatriz(f)

    # Imprime a matriz e o vetor de entrada
    printMatriz(matriz)
    print(vetorB)

    # Resolve o sistema usando o método de Jacobi
    precisao = 1e-4
    maxIteracoes = 100
    vetorX = metodoJacobi(matriz, vetorB, precisao, maxIteracoes)

    # Imprime o vetor solução
    print(vetorX)

    # Escreve o vetor solução no arquivo de saída
    fOutput = open("resultado.txt", "w")
    for i in vetorX:
        fOutput.write(f"{i:.3f}\n")
    fOutput.close()

if __name__ == "__main__":
    main()
