import csv
import gzip
import shutil

# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.
# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o suficiente.
# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro.

# 1

def define_default_city(state):
    with open('capitais-BR.csv', 'r') as capitais:
        ler = csv.reader(capitais)
        for linha in ler:
            fl = linha[0].split(';')
            dkey = fl[0]
            if(state == dkey):
                return True
            else:
                return False

# 2

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
        



# 3


def descompactar():
    with gzip.open("lista-cpf.txt.tar.gz", 'r') as entrada:
        with open('cpfs.txt', 'wb') as saida:
            shutil.copyfileobj(entrada, saida)


def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def separarCPF():
    descompactar()
    listinha = []
    with open("cpfs.txt", 'r') as cpfs:
        for listacpf in cpfs:
            listinha.append(listacpf)
                
    listinha.sort()
    for i in range(0, len(listinha)):
        listinha[i] = listinha[i].replace('\n', "")

    listinha = remove_repetidos(listinha)
    arquivo = open('CPFsInteiros.txt', 'w')
    for l in range(0, len(listinha)):
        arquivo.write(listinha[l] + "\n")
        
    arquivo.close()
    
    



