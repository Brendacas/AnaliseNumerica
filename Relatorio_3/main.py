import numpy as np


def processar_arquivos_entradas():
  with open("entrada.txt", "r") as arq:
    Ta, valores_T, x_final, h, n = [], [], [], [], []

    for linha in arq:
      aux = linha.strip().split(";")
      Ta.append(eval(aux[0]))

      valores_T_aux = list(map(eval, aux[1].split(",")))
      valores_T.append(valores_T_aux)

      x_final.append(eval(aux[2]))
      h.append(eval(aux[3]))

      n_aux = eval(aux[4])
      n.append(n_aux)

  return Ta, valores_T, x_final, h, n


def diferencas_finitas(Ta, valores_T, delta_x, h, n):
  A = np.zeros((n - 1, n - 1))
  b = np.zeros(n - 1)

  for i in range(n - 1):
    for j in range(n - 1):
      if i == j:
        A[i, j] = 2 + h * delta_x**2
        if j - 1 >= 0:
          A[i, j - 1] = -1
        if j + 1 < n - 1:
          A[i, j + 1] = -1

  for i in range(n - 1):
    if i == 0:
      b[i] = h * (delta_x**2) * Ta + valores_T[0]
    elif i == n - 2:
      b[i] = h * (delta_x**2) * Ta + valores_T[1]
    else:
      b[i] = h * (delta_x**2) * Ta

  result = np.linalg.solve(A, b)
  result = np.insert(result, 0, valores_T[0])
  result = np.append(result, valores_T[1])

  resultado = list(enumerate(map(lambda x: round(x, 3), result)))
  return resultado


def main():
  Ta, valores_T, x_final, h, n = processar_arquivos_entradas()
  with open("saidas.txt", "w") as arq:
    for i, (Ta_val, valores_T_val, x_final_val, h_val,
            n_val) in enumerate(zip(Ta, valores_T, x_final, h, n)):
      resultado = diferencas_finitas(Ta_val, valores_T_val, x_final_val / n_val,
                                    h_val, n_val)
      arq.write(f"{resultado}\n")
  arq.close()
if __name__ == "__main__":
  main()
