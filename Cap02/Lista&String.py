# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
# Exercício 5 - Crie um dicionário vazio e imprima na tela
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
# frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

# questão 1 
lista= [1,2,3,4,5,6,7,8,9,10]
print(lista)

# questão 2
""" listaO=["casa", "carro", "bicicleta", "batom", "sapato"]
print(listaO) """

# questão 3
""" frase=("Eu sou uma estudante de sistemas para internet")
frase1=(" do segundo período da Unicap")
print(frase+frase1)
 """
# questão 4 
""" n=(1, 25, 2, 3, 4, 4, 4, )
len(n)
print(n.count(4)) """

# questão 5
""" dic={}
print(dic) """

# questão 6
""" dic1={'Nome':'Vanessa','idade':20, 'endereço':'Salgadinho'}
print(dic1) """

# questão 7
""" dic2={'Sobrenome':'Ferreira'}
print(dic1.update(dic2)) """

# questão 8
""" dicionario={'Vanessa':20 , 'Carla':21 , 'idade':[20,21]}
print(dicionario) """

# questão 9
""" lista1=['Vanessa', (1,2), {'meta':'casa', 'realidade':'sonho'}, 2.5]
print(lista1) """

# questão 10
""" frase_teste="Cientista de dados é o profissional mais sexy do século XXI".strip()
print(frase_teste[1:19]) """