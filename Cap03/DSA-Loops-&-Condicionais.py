# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# Exercícios - Loops e Condiconais
# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
# temperatura = float(input('Qual a temperatura? '))
# if temperatura > 30:
# print('Vista roupas leves.')
# else
#     print('Busque seus casacos.')
# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

# Resultados

# Questão1
diaSemana=input('Que dia da semana é hoje? ').upper()
if diaSemana=="SÁBADO" or diaSemana=='DOMINGO':
    print('Hoje é dia de descanso!')
else:
    print('Você precisa trabalhar!')

# Questão2
# frutas=['maça','uva','laranja','banana']
# print('morango' in(frutas))

# Questão3
# tupl=(4*2,5*2,6*2,7*2)
# lista=list(tupl)
# print(lista)

# Questão4
# for i in range(100, 150,2):
#     print(i)

# Questão5
# for t in range(1,41):
#     if t>=35 and t<=40:
#      print(t)
#      t+=1
    
# Questão6
# counter=0
# while counter<100:
#     if counter==23:
#         break
#     print(counter)
#     counter+=1

#Questão7
# lista=[]
# var=4
# while var<=20:
#     if var%2==0:
#      lista.append(var)
#      var+=2
# print(lista)

# Questão8
# lista=[]
# for i in range(5,45,2):
#     lista.append(i)
# print(lista)
# i+=1

# Questão9
# temperatura = float(input('Qual a temperatura? '))
# if temperatura > 30:
#     print('Vista roupas leves.')
# else:
#     print('Busque seus casacos.')




# Questão10
# frase=('É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir.')
# print("O número de vezes que a letra R aparece na frase é {}".format(frase.count('r')))