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


def PosiçãoFalsa(fx, xsup, xinf, erro):
    # Verifica a continuidade da função no intervalo inicial.
    if fx.aplicaValor(xsup) * fx.aplicaValor(xinf) >= 0:
        raise Exception("A função não tem uma raiz no intervalo inicial.")
    # Verifica se o erro tolerado é maior que zero.
    if erro <= 0:
        raise Exception("O erro tolerado deve ser maior que zero.")
    # Verifica se o intervalo inicial é válido.
    if xsup == xinf:
        raise Exception("O intervalo inicial é vazio.")

    fxsup = fx.aplicaValor(xsup)
    fxinf = fx.aplicaValor(xinf)
    xr = xsup - (fxsup * (xinf - xsup) / (fxinf - fxsup))
    fxr = fx.aplicaValor(xr)
    eu = fabs((xr - xsup) / xr)
    ea = fabs((xr - xinf) / xr)

    if fxsup * fxinf > 0:
        raise Exception

    while eu >= erro and ea >= erro:
        if fxinf * fxr < 0:
            xsup = xr
        elif fxinf * fxr > 0:
            xinf = xr

        fxsup = fx.aplicaValor(xsup)
        fxr = fx.aplicaValor(xr)
        fxinf = fx.aplicaValor(xinf)
        xr = xsup - (fxsup * (xinf - xsup) / (fxinf - fxsup))
        eu = fabs((xr - xsup) / xr)
        ea = fabs((xr - xinf) / xr)

    errosEstimados = [ea, eu]
    errosEstimados.sort()
    return xr, errosEstimados[0]


def processar_arquivo_entrada():
    with open("entrada.txt", mode="r") as f:
        texto = f.readlines()

        expr = texto[0].strip("\n")
        xsup = float(texto[1].strip("\n").split(" ")[0])
        xinf = float(texto[1].strip("\n").split(" ")[1])
        erro = float(texto[2])

    return expr, xsup, xinf, erro


def criar_saida(fx, xr, erro):
    f = open("resultado.txt", "w")
    f.write(f' Xr: {xr:.5f}\n ')
    f.write(f'Erro tolerado: {erro}\n')
    f.write(f'Erro Aproximado: {ea:.5f}\n')
    f.close()


#### main

expr, xsup, xinf, erro = processar_arquivo_entrada()
fx = FuncaoAlgebrica(expr)
try:
    xr, ea = PosiçãoFalsa(fx, xsup, xinf, erro)
    print(f"Xr: {xr:.5f} Erro Estimado: {ea:.5f} Erro tolerado: {erro}")
    criar_saida(expr, xr, erro)
except:
    print("Não foi possivel realizar operação, valores contraditorios")
