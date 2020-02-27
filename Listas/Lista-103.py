###
# Exercicios
###

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string

tituloSplit = book1.split("by")

tituloSplit2 = book2.split("by")

tituloSplit3 = book3.split("by Nassim")

# 2) Salve o titulo de cada livro em uma variável
titulo = tituloSplit[0]
titulo2= tituloSplit2[0]
titulo3 = tituloSplit3[0]
resto = tituloSplit[1]
resto2 = tituloSplit2[1]
resto3 = tituloSplit3[1]

print("Título 1:", titulo)
print("Titulo 2:", titulo2)
print("Título 3:", titulo3)

# 3) Quantos caracteres cada título tem?
print("Caracteres de cada título:")
print("Título 1:", len(titulo))
print("Título 2:", len(titulo2))
print("Título 3:", len(titulo3))

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
autor, ano = resto.split(',')
autor2, ano2 = resto2.split(',')
autor3, ano3 = resto3.split(',')

msg = '{0} - {1}, {2}'.format(titulo, autor, ano)
msg2 = '{0} - {1}, {2}'.format(titulo2, autor2, ano2)
msg3 = '{0} - {1}, {2}'.format(titulo3, autor3, ano3)
print(msg)
print(msg2)
print(msg3)


# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

palindrome_one = palindrome_one.replace(' ', '')
palindrome_one_inverted = palindrome_one[::-1]
if palindrome_one_inverted == palindrome_one:
        print (palindrome_one, "é um palindromo")
else:
        print (palindrome_one, "não é um palindromo")

palindrome_two = palindrome_two.lower().replace(' ', '')
palindrome_two_inverted = palindrome_two[::-1]
if palindrome_two_inverted == palindrome_two:
        print (palindrome_two, "é um palindromo")
else:
        print (palindrome_two, "não é um palindromo")

palindrome_three = palindrome_three.lower().replace(' ', '')
palindrome_three_inverted = palindrome_three[::-1]
if palindrome_three_inverted == palindrome_three:
        print (palindrome_three, "é um palindromo")
else:
        print (palindrome_three, "não é um palindromo")
        
palindrome_four = palindrome_four.lower().replace(' ', '')
palindrome_four_inverted = palindrome_four[::-1]
if palindrome_four_inverted == palindrome_four:
        print (palindrome_four, "é um palindromo")
else:
        print (palindrome_four, "não é um palindromo")

