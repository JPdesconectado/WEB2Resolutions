professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
print(type(professor1))
print(professor1)

# Tamanho
print(len(professor1))
# Chaves
print(professor1.keys())
# Valores
print(professor1.values())

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

# Primeira disciplina
print(professor2['courses'][0])

# Utilizando construtor
professor3 = dict(id=28, name='Jorge Armino', idade=37)
print(type(professor3))
print(professor3)

# adicionando chave e valor em um dict jah existente
professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']
print(professor3)

# Acessar um valor em um dict
print(professor1['state_origin'])


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



# 3

professor1['Latitude'] = '90'
professor1['Longitude'] = '0'
professor2['Latitude'] = '50'
professor2['Longitude'] = '25'
professor3['Latitude'] = '190'
professor3['Longitude'] = '45'