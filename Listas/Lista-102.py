days_list = ['mon','tues','wed','thurs','fri', 'sat', 'sun']
list = ['a', 1, 3.14159265359]

print("Dias da semana:", days_list)
print("Lista 2:", list)
print("--------------------")
print("Exercícios")

# Como selecionar 'wed' pelo indice?
print("Questão 01:", days_list[2])

# Como verificar o tipo de 'mon'?
print("Questão 02:", type(days_list[days_list.index('mon')]))

# Como separar 'wed' até 'fri'?
a = days_list.index('wed')
b = days_list.index('fri')+1
print("Questão 03:", days_list[a:b])

# Quais as maneiras de selecionar 'fri' por indice?
print("Questão 04:", days_list[4])

# Qual eh o tamanho dos dias e days_list?
print("Questão 05:", len(days_list))

# Como inverter a ordem dos dias?
days_list.reverse()
print("Questão 06:", days_list)

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
list.insert(1, 'zero')
print("Questão 07:", list)

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
ultimo_elemento = list.pop()
print("Questão 08:", list)
print('Elemento removido: ', ultimo_elemento)

# Como limpar list?
list.clear()
print("Questão 09:", list)

# Como deletar list?
del(list)
print("Questão 10: Lista Deletada.")