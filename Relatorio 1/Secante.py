from sympy import sympify, symbols
from math import fabs


class FuncaoAlgebrica:

    def __init__(self, str_expr):
        self.__x = symbols("x")
        self.__expr = sympify(str_expr)

    def aplicaValor(self, x1):
        return self.__expr.subs(self.__x, x1)

    def printFx(self):
        return self.__expr


def secante(fx, xi, x_1, erro):
    """
    Calcula a raiz de uma função usando o método da secante.

    Args:
        fx: Uma função SymPy.
        xi: Uma aproximação inicial da raiz.
        x_1: Outra aproximação inicial da raiz.
        erro: O erro tolerado.
    """

    fxi = fx.aplicaValor(xi)
    fx_1 = fx.aplicaValor(x_1)

    xi_1 = xi - (fxi * (x_1 - xi)) / (fx_1 - fxi)

    ea = fabs((xi_1 - xi) / xi_1) * 100
    while ea >= erro:
        x_1 = xi
        xi = xi_1
        fxi = fx.aplicaValor(xi)
        fx_1 = fx.aplicaValor(x_1)
        xi_1 = xi - (fxi * (x_1 - xi)) / (fx_1 - fxi)
        ea = fabs((xi_1 - xi) / xi_1) * 100

    return xi_1, ea


def processar_arquivo_entrada():
    with open("entrada.txt", mode="r") as f:
        texto = f.readlines()

    expr = texto[0].strip("\n")
    xi = float(texto[1].strip("\n").split(" ")[0])
    xi_1 = float(texto[1].strip("\n").split(" ")[1])
    erro = float(texto[2])
    f.close()
    return expr, xi, xi_1, erro


def criar_saida(fx, xr, ea, erro):
    f = open("resultado.txt", mode="w")
    f.write(f"Xr: {xr:.5f}\n")
    f.write(f"Erro aproximado: {ea:.5f}\n")
    f.write(f"Erro tolerado: {erro:.5f}\n")
    if ea > erro:
        f.write("Erro maior que o erro tolerado.\n")
    f.close()


#### main


expr, xi, xi_1, erro = processar_arquivo_entrada()
fx = FuncaoAlgebrica(expr)

xr, ea = secante(fx, xi, xi_1, erro)
print(f"Xr: {xr} Erro Estimado: {ea:.5} Erro tolerado: {erro}")
criar_saida(fx, xr, ea, erro)

