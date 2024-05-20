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
	
def trocar(matriz,vetor,a,b,mij):
# a = Linha Atual b= Linha Antiga
		colunas = len(matriz[0])
		print(f'vetor-({a+1}) = {vetor[a]} - {vetor[b]}')
		vetor[a] = vetor[a] - vetor[b]*mij

		for coluna in range(0,colunas):
			matriz[a][coluna] = matriz[a][coluna] - matriz[b][coluna]*mij	
			
def permuta(matriz,vetor,linhaAtual,coluna):
	for j in range(0,len(matriz[0])):
		matriz[coluna][j],matriz[linhaAtual][j] = matriz[linhaAtual][j],matriz[coluna][j]
	vetor[coluna],vetor[linhaAtual] = vetor[linhaAtual],vetor[coluna]
	
def transformarEmTriangular(matriz,vetor):
	for i, linha in enumerate(matriz):
		mij=0
		for j,coluna in enumerate(linha):
			if( i > j):
				if(matriz[j][j]==0):
						permuta(matriz,vetor,i,j)
				else:
						mij = (matriz[i][j] / matriz[j][j])
						trocar(matriz,vetor,i,j,mij)
			
	
def iteracaoResultados(matriz, vetor):
	tamVetorResposta = len(vetor)
	vetorResultados = [0.0]*(tamVetorResposta)
	vetorResultados[tamVetorResposta-1] = vetor[tamVetorResposta-1]/matriz[tamVetorResposta-1][tamVetorResposta-1]
	for i in range(tamVetorResposta-2,-1,-1):
		r = vetor[i]
		for a in range(tamVetorResposta-1,-1,-1):
			r += (vetorResultados[a])*(-matriz[i][a])
		vetorResultados[i] = r/matriz[i][i]
	return vetorResultados

## main		
f = open("entrada.txt","r")
foutput = open("resultado.txt","w")

matriz,vetorB = gerarMatriz(f)
transformarEmTriangular(matriz,vetorB)
valorX = iteracaoResultados(matriz,vetorB)
for r,i in enumerate(valorX):
	foutput.write(f'Valor de X{r}: {i:.3f}\n')