import csv

# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.
# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o suficiente.
# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro.

def remover():
    with open("capitais-BR.csv", 'r', encoding='utf8') as capitaisIn:
        estados = csv.reader(capitaisIn, delimiter=';')
        lista = list(estados)
        print(lista)
        lista.remove(['Rio de Janeiro', 'Rio de Janeiro'])
        lista.remove(['Minas Gerais', 'Belo Horizonte'])
        lista.remove(['Espírito Santo', 'Vitória'])
        lista.remove(['São Paulo', 'São Paulo'])
        print(lista)

    with open("capitais-BR.csv", 'w', encoding='utf8') as capitaisOut:
        writer = csv.writer(capitaisOut)
        writer.writerows(lista)
        
remover()