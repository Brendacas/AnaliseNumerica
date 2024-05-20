import re
def gerarMatriz(f):
	vetorResultante = []
	matriz = []

	texto = f.readlines()
	tamSistema = len(texto)-1
	
	vetorResultante = [float(i) for i in re.findall("([\+ | \-]*[0-9]+[\.]*[0-9]*)", texto[tamSistema])]
	for a in range(tamSistema):
		linha =[float(i) for i in re.findall("([\+ | \-]*[0-9]+[\.]*[0-9]*)", texto[a])]
		matriz.append(linha)

	return matriz,vetorResultante
def printMatriz(matriz):
	for i in matriz:
		print(i)
	print("\n")
	
'''Metodo que realiza a troca das linhas'''
def trocar(matriz,vetor,a,b,mij):
        # a=Linha Nova, b = Linha Antiga
		colunas = len(matriz[0])
		vetor[a] = vetor[a] - vetor[b]*mij

		for coluna in range(0,colunas):
			matriz[a][coluna] = matriz[a][coluna] - matriz[b][coluna]*mij	
			
def permuta(matriz,vetor,linhaAtual,coluna):
	for j in range(0,len(matriz[0])):
		matriz[coluna][j],matriz[linhaAtual][j] = matriz[linhaAtual][j],matriz[coluna][j]
	vetor[coluna],vetor[linhaAtual] = vetor[linhaAtual],vetor[coluna]
	
def matrizL(tam):
	matrizL = []

	for i in range(0,tam):
		matrizL = matrizL + [[0]*3]
		for j in range(0,tam):
			if i==j:
				matrizL[i][j]=1
	return matrizL

def fatorarEmLU(matrizOrig,Lu,vetor):
	for i, linha in enumerate(matrizOrig):
		mij=0
		for j, coluna in enumerate(linha):
			if( i > j):
				if(matrizOrig[j][j]==0):
						permuta(matrizOrig,vetor,i,j)
				else:
						mij = (matrizOrig[i][j] / matriz[j][j])
						matrizEntradaL[i][j]=mij
						trocar(matrizOrig,vetor,i,j,mij)
	return matrizEntradaL,matrizOrig
	
def iteracaoResultadosRegressiva(matriz, vetor):
	tamVetorResposta = len(vetor)
	vetorResultados = [0.0]*(tamVetorResposta)
	vetorResultados[tamVetorResposta-1] = vetor[tamVetorResposta-1]/matriz[tamVetorResposta-1][tamVetorResposta-1]
	for i in range(tamVetorResposta-2,-1,-1):
		r = vetor[i]
		for a in range(tamVetorResposta-1,-1,-1):
			r += (vetorResultados[a])*(-matriz[i][a])
		vetorResultados[i] = r/matriz[i][i]
	return vetorResultados

def iteracaoResultadosProgressivo(matriz, vetor):
	tamVetorResposta = len(vetor)
	vetorResultados = [0.0]*(tamVetorResposta)
	vetorResultados[0] = vetor[0]/matriz[0][0]
	for i in range(1,tamVetorResposta):
		r = vetor[i]
		for a in range(0,i):
			r += (vetorResultados[a])*(-matriz[i][a])
		vetorResultados[i] = r
	return vetorResultados	

## main		
f = open("entrada.txt","r")
fOutput = open("resultado.txt","w")

matriz,vetorB = gerarMatriz(f)

matrizEntradaL = matrizL(len(vetorB))
L,U = fatorarEmLU(matriz,matrizEntradaL,vetorB)
print("Vetor B:")
print(vetorB)
printMatriz(L)
D = iteracaoResultadosProgressivo(L,vetorB)
print(f'D: {D}')
printMatriz(U)
X = iteracaoResultadosRegressiva(U,D)
print(X)

#Resultado no arquivo
for r,i in enumerate(X):
	fOutput.write(f'Valor de X{r}: {i:.3f}\n')