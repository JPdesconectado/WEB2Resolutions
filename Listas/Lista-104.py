###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
#
lista1 = ['a', 'b', 'c', 'd', 'e']
lista2 = ['a', 'b', 'c', 'd', 'e']
    
    
def func(l1, l2):
    if(l1 == l2):
        return True
    else:
        return False
    
print(func(lista1,lista2))
 
    
# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
#
str ='caneta azul'

def func(str):
    str = str.lower().replace(' ','')
    if(str == str[::-1]):
        return True
    else:
        return False
    
    
print(func(str))

# OBS.: Utilize apenas o que foi estudado ate agora
    