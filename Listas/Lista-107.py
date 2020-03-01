###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla.
# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py


# lista
list = [2, 3, 5, 7, 11, 13, 17, 19]
# tupla
tuple = (2, 3, 5, 7, 11, 13, 17, 19)



print("----------- LISTA -------------")
print("Lista:", list)

print("Inserindo elemento no final da Lista:")
list.append(22)
print(list)

print("Concatenando Listas:")
list.extend(list)
print(list)

print("Inserindo elementos em determinada posição:")
list.insert(0, 0)
print(list)

print("Removendo elementos:")
list.remove(0)
print(list)


print("Remove o item que está no indice passado:")
list.pop()
print(list)


print("Descobrindo o índice do número 7 na Lista:")
print(list.index(7))

print("contando quantas vezes o número 2 aparece na Lista:")
print(list.count(2))

print("Invertendo lista:")
list.reverse()
print(list)

print("Ordenando elementos:")
list.sort()
print(list)

print("----------- TUPLA -------------")
print("Tupla:", tuple)


print("Tuplas são imutáveis em sua maioria, com raras exceções, por isso todos os métodos que existem na lista de manipulação, não podem ser utilizados nas tuplas.")

# tuple.append(22)
# tuple.extend(tuple)
# tuple.insert(0, 0)
# tuple.remove(0)
# tuple.pop()
print("Descobrindo o índice do número 7 na Tupla:")
print(tuple.index(7))

print("contando quantas vezes o número 2 aparece na Tupla:")
print(tuple.count(2))

# tuple.reverse()
# tuple.sort()