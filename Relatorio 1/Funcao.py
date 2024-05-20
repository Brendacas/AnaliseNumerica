from sympy import symbols, sympify

class FuncaoAlgebrica:
    def __init__(self, str_expr):
        self._x = symbols("X")
        self.expr = sympify(str_expr)

    def aplica_Valor(self, X1):
        return self._expr.subs(self._x, X1)

    def printFuncao(self):
        return self._expr
    
