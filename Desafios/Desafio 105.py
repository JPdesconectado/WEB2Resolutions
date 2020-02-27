import time

'''
	DESAFIO!!!
	
	
'''

'''
Questão 1
1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
'''

x = 0
lista = []

def numPares(x):
    if x % 2 == 0:
        lista.append(x)
        x = x + 1
    
    else:
        x = x + 1
    
    if x == 0 or len(lista) == 1000:
        return 1
    
    else:
        numPares(x)
    

numPares(x) 
    

time.sleep(1)
'''
Questão 2
2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. 
Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

print('Questão 2')

lista2 = []

for z in range(9999):
    lista2.append(z)

for c in lista2:
    if (c % 5 == 0):
        print('O primeiro múltiplo de 5 é:' , c)
        break;

'''
Questão 3
3) Pesquise sobre generators (yield)
'''

print('questão 3')


'''
Questão 4
4) Pesquise sobre lambda, map, zip
'''

print('questão 4')
        