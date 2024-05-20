def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]
        if all(abs(x[i] - x0[i]) < tol for i in range(n)):
            return x
        x0 = x.copy()
    raise ValueError("O método de Gauss-Seidel não convergiu")


def processar_arquivo_entrada(f):
    matriz = []
    with open(f, "r") as f:
        for line in f:
            row = [float(x) for x in line.strip().split()]
            matriz.append(row)
    return matriz

def criar_Saida(f, solucao):
    with open(f, "w") as f:
        for value in solucao:
            f.write(f"{value}\n")

if __name__ == "__main__":
    entrada = "entrada.txt"
    saida = "resultado.txt"
    tol = 1e-6
    max_iter = 1000

    A = processar_arquivo_entrada(entrada)
    b = [row[-1] for row in A]
    A = [row[:-1] for row in A]
    x0 = [0.0] * len(b)

    try:
        solucao = gauss_seidel(A, b, x0, tol, max_iter)
        criar_Saida(saida, solucao)
        print(saida)
    except ValueError as e:
        print(e)
