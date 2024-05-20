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


def heun(funcao, valor_y, intervalo, h, iteracoes=1):
    x, y = symbols('x y')
    saida = []

    valor_x = intervalo[0]
    while valor_x < intervalo[1]:
        y_predito = valor_y

        for _ in range(iteracoes):
            gradiente_inicial = funcao.subs({x: valor_x, y: y_predito})
            y_predito_tentativa = valor_y + h * gradiente_inicial

            gradiente_final = funcao.subs({x: valor_x + h, y: y_predito_tentativa})
            y_predito = valor_y + (h / 2) * (gradiente_inicial + gradiente_final)

        valor_y = y_predito
        valor_y = round(valor_y, 3)
        saida.append([round(valor_x, 3), valor_y])
        valor_x = round(valor_x + h, 3)

    return saida

def main():
    funcao, y_inicial, intervalo, h = processar_arquivo_entradas()

    with open("saidas.txt", "w") as arq:
        for i in range(len(funcao)):
            resultado = heun(funcao[i], y_inicial[i], intervalo[i], h[i], iteracoes=2)
            arq.write(f"Resultado para função {i + 1}:\n")
            arq.write(str(resultado) + "\n")
            if i < len(funcao) - 1:
                arq.write("\n")

if __name__ == "__main__":
    main()
