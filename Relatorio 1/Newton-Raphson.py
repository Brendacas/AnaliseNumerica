from sympy import sympify, symbols, diff
from math import fabs


class FuncaoAlgebrica:

    def __init__(self, str_expr):
        self.__x = symbols("x")
        self.__expr = sympify(str_expr)

    def aplicaValor(self, x1):
        return self.__expr.subs(self.__x, x1)

    def derivada(self, x):
        dx = diff(self.__expr, self.__x)
        return dx.subs(self.__x, x)

    def printFx(self):
        return self.__expr


def NewtonRaphson(fx, xi, erro):
    maxIter = 0
    fxi = fx.aplicaValor(xi)
    fdx = fx.derivada(xi)
    if fdx == 0:
        raise Exception("Derivada é igual a zero em x0.")

    xi_1 = xi - (fxi / fdx)
    ea = fabs((xi_1 - xi) / xi_1) * 100
    maxIter += 1
    while ea >= erro and maxIter < 50:
        xi = xi_1
        fxi = fx.aplicaValor(xi)
        fdx = fx.derivada(xi)
        if fdx == 0:
            raise Exception("Derivada é igual a zero em xn.")
        xi_1 = xi - (fxi / fdx)
        ea = fabs((xi_1 - xi) / xi_1) * 100

    return xi_1, ea


def processar_arquivo_entrada():
    with open("entrada.txt", mode="r") as f:
        texto = f.readlines()

    expr = texto[0].strip("\n")
    xi = float(texto[1].strip("\n").split(" ")[0])
    erro = float(texto[2].strip("\n"))
    f.close()
    return expr, xi, erro


def criar_saida(xr, ea, erro):
    f = open("resultado.txt", mode="w")
    f.write(f"Xr: {xr:.5f}\n")
    f.write(f"Erro aproximado: {ea:.5f}\n")
    f.write(f"Erro tolerado: {erro}")
    f.close()


#### main

expr, xi, erro = processar_arquivo_entrada()
fx = FuncaoAlgebrica(expr)
print(fx.printFx())
try:
    xr, ea = NewtonRaphson(fx, xi, erro)
    print(f"Xr: {xr:.5f} Erro Estimado: {ea:.5f} Erro tolerado: {erro}")
except Exception as e:
    print(str(e))
criar_saida(xr, ea, erro)
