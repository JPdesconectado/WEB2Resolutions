
###
# Exercicios
###
    

## Usando a 
lista = ['a','b','c']
# 1) Faca um loop para retornar: ['A','B','C']
for i in lista:
    lista[lista.index(i)] = i.upper()
print(lista)

## Usando os 
numeros = [0, 1, 3, 4, 5]
# 2) Faca um loop para retornar a soma de todos os elementos da listas
soma=0
for i in numeros:
    soma+=i
print(soma)
# 3) Faca um loop para retornar apenas os numeros impares
for i in numeros:
    if(i%2 == 0):
        numeros.remove(i)
print(numeros)

## usando a 
string = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string
count = 0
for i in string.replace(',','').split(' '):
    if(len(i) >= 5):
        count+= 1
print(count)
# 3) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100

lista = [i * 3 for i in range(100) if (i*3) <= 100]
print(lista)