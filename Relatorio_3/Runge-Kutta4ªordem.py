from sympy import symbols


def processar_arquivo_entradas():
  arq = open("entrada.txt", "r")
  x, y = symbols('x y')

  funcao = []
  y_inicial = []
  intervalo = []
  h = []

  linha = None
  while linha != '':
    linha = arq.readline()
    if linha != "":
      aux = linha.split(";")
      funcao_aux = eval(aux[0])
      y_inicial_aux = eval(aux[1])

      intervalo_aux = aux[2]
      intervalo_aux = intervalo_aux.split(",")
      intervalo_aux = [eval(x) for x in intervalo_aux]

      h_aux = aux[3]
      h_aux = h_aux.split("\n")
      h_aux = eval(h_aux[0])

      funcao.append(funcao_aux)
      y_inicial.append(y_inicial_aux)
      intervalo.append(intervalo_aux)
      h.append(h_aux)
  arq.close()

  return funcao, y_inicial, intervalo, h


def runge_kutta_4_ordem(funcao, valor_y, intervalo, h):
  x, y = symbols('x y')
  saida = []

  valor_x = intervalo[0]
  while valor_x < intervalo[1]:
    k1 = h * funcao.subs({x: valor_x, y: valor_y})
    k2 = h * funcao.subs({x: valor_x + h / 2, y: valor_y + k1 / 2})
    k3 = h * funcao.subs({x: valor_x + h / 2, y: valor_y + k2 / 2})
    k4 = h * funcao.subs({x: valor_x + h, y: valor_y + k3})

    valor_y = valor_y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    valor_y = round(valor_y, 3)
    saida.append([round(valor_x, 3), valor_y])
    valor_x = round(valor_x + h, 3)

  return saida


def main():
  funcao, y_inicial, intervalo, h = processar_arquivo_entradas()

  with open("saidas.txt", "w") as arq:
    for i in range(len(funcao)):
      resultado = runge_kutta_4_ordem(funcao[i], y_inicial[i], intervalo[i],
                                      h[i])
      arq.write(f"Resultado para função {i + 1}:\n")
      arq.write(str(resultado) + "\n")
      if i < len(funcao) - 1:
        arq.write("\n")


if __name__ == "__main__":
  main()
