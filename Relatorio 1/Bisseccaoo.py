import sympy
from math import fabs

class FuncaoAlgebrica:
    def __init__(self, str_expr):
        self._x = sympy.symbols("x")
        self._expr = sympy.sympify(str_expr)

    def aplica_valor(self, x1):
        return self._expr.subs(self._x, x1)

    def print_fx(self):
        return self._expr

def calcular_erro(x1, x2):
    return fabs((x2 - x1) / (x2 + x1)) * 100

def bisseccao(fx, xsup, xinf, erro):
    """
    Calcula a raiz da função fx no intervalo [xinf, xsup] com tolerância erro.

    Args:
        fx: Função a ser calculada.
        xsup: Extremo superior do intervalo.
        xinf: Extremo inferior do intervalo.
        erro: Tolerância de erro.

    Returns:
        raiz, erro tolerado e erro aproximado.
    """

    ea = calcular_erro(xinf, xsup)
    xr = (xsup + xinf) / 2
    fx1 = fx.aplica_valor(xinf)
    fx2 = fx.aplica_valor(xr)

    while ea > erro:
        if fx1 * fx2 > 0:
            xinf = xr
        elif fx1 * fx2 < 0:
            xsup = xr
        else:
            return xr, ea

        xr = (xsup + xinf) / 2
        ea = calcular_erro(xinf, xsup)
        fx1 = fx.aplica_valor(xinf)
        fx2 = fx.aplica_valor(xr)

    return xr, ea

def processar_arquivo_entrada():
    with open("entrada.txt", mode="r") as f:
        texto = f.readlines()

        expr = texto[0].strip("\n")
        xsup = float(texto[1].strip("\n").split(" ")[0])
        xinf = float(texto[1].strip("\n").split(" ")[1])
        erro = float(texto[2])

    return expr, xsup, xinf, erro

def criar_saida(fx, xr, erro):
    with open("resultado.txt", mode="w") as f:
        f.write(f' Xr: {xr:.5f}\n ')
        f.write(f'Erro tolerado: {erro}\n')
        f.write(f'Erro Aproximado: {ea:.5f}\n')
        f.close()

#### main

expr, xsup, xinf, erro = processar_arquivo_entrada()
fx = FuncaoAlgebrica(expr)

xr, ea = bisseccao(fx, xsup, xinf, erro)

print(f"Xr: {xr:.5f} Erro Aproximado: {ea:.5f} Erro Tolerado: {erro:.5f}")
criar_saida(expr, xr, erro)
