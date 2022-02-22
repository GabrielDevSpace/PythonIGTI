# -*- coding: utf-8 -*-
"""
Coleções de dados em Python
+Lists - è uma coleção que é ordenada e imutável Permite dados Duplicados
Identificador: []

+Tuples - Isso significa que quando uma tupla é criada não é possível adicionar,
alterar ou remover seus elementos.
Geralmente, ela é utilizada para adicionar tipos diferentes de informações,
porém, com a quantidade de elementos definidos.
Identificador: ()

+Sets - è uma coleção que NÂO é ordenada e desindexada - Sem dados Duplicados
Identificador: {}

+Dictionary - è uma coleção que é desordenada e mutavel - Sem dados Duplicados
Identificador {chave:valor}
"""

# Lists
vocabulario = ["escolha", "selecao", "controle"]
numeros = [17, 123]
vazia = []
lista_mista = ["ola", 2.0, 5*2, [10, 20]]

print("Lists: ")
print(numeros)
print(lista_mista)
numeros.append("10")  # adicionando itens na lista numeros
nova_lista = [numeros, vocabulario]
print(nova_lista)

print("\n")

# Tuples
tuples_list = ["10", "segunda-feita", "Fevereiro", 2022]
tuples_numbers = [10, 15, 20]
tupla_ajuntadas = tuples_list + tuples_numbers
print("Tuples: ")
print(tupla_ajuntadas)
print("\n")

# sets
c = {'Paula', 'Erica', 'Marcio'}
b = {'Ana', 'João', 'Paula'}
a = c | b

print("Sets: ")
print(a)
print("\n")

# dictionary
my_dictionary = { "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print("Dictionary: ")
print(my_dictionary["electric"])
