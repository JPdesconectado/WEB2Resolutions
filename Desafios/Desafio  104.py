
'''
	DESAFIO!!!
	1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
	2) Agora faca sem utilizar uma terceira variavel temporaria.
	OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''


''' 
1)
'''
print('-- Questão 1 --')

x = 10
y = 5

print('valor antigo de x:' , x)
print('valor antigo de y:' ,y)

z = y
y = x
x = z

print('valor de x:' , x)
print('valor de y:' ,y)

'''
2)
'''

print('-- Questão 2 --')

x2 = 'funciona'
y2 = 'não'

print('Antigo x: ' , x2)
print('Antigo y: ' , y2)

def trocar(x2, y2):
    return y2, x2


x2, y2 = trocar(x2, y2)

print('Novo x: ' , x2)
print('Novo y: ' , y2)