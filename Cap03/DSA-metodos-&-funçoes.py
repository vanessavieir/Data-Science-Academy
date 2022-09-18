# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números      
# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista
# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
# total = 0
# def soma( arg1, arg2 ):
#     total = arg1 + arg2; 
#     print ("Dentro da função o total é: ", total)
#     return total;


# soma( 10, 20 );
# print ("Fora da função o total é: ", total)
# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
# Celsius = [39.2, 36.5, 37.3, 37.8]
# Fahrenheit = map(coloque_aqui_sua_função_lambda)
# print (list(Fahrenheit))
# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário
# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.
# import pandas as pd
# dir(pd)
# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
# import pandas as pd
# file_name = "binary.csv"



# Questao1
# def contagem():
#     for i in range(2,21):
#         if (i%2==0):
#             print(i)

# contagem()

# Questao2
# def string(frase):
#     return frase.upper()

# frase='Você é uma boa garota e realizará todos os seus sonhos!'

# print(string(frase))


# Questao3
# def lista (valores):
#     return (valores+valores2)

# valores2=[5,6]
# valores=[1,2,3,4]

# print(lista(valores))

# Questao4
# def formal(element, *lista):
#    print(element)
#    for i in lista:
#     print((i))
#    return;
# print(formal(10))
# #print(formal(1,2,3,4))


# Questao5
# def valores (valor1,valor2):
#     soma=valor1+valor2;
#     print('A soma dos valores equivale a: {} '.format(soma))
#     return soma;

# (valores(50,200))



# Compreendendo exemplo
# total = 0
# def soma( arg1, arg2 ):
#      total = arg1 + arg2; 
#      print ("Dentro da função o total é: ", total)
#      return total;


# soma( 10, 20 );
# print ("Fora da função o total é: ", total)


# Questao7
Celsius = [39.2, 36.5, 37.3, 37.8]
farenheit=map(lambda formula: (float(9 / 5))*formula + 32, Celsius)
print(list(farenheit))
