#operadores logicos:
'''
Possuem a capacidade de unir expressões lógicas e, assim, formar uma nova
expressão
'''

'''
--> 'and' (e)
--> 'or' (ou)
--> 'not' (negação) {podemos utilizar para inverter resultados}
--> 'is' (é)
--> 'is not' (não é) {podemos utilizar para, por exemplo, checar se uma variável é de um tipo específico}
--> 'in' (está contido)
--> 'not in' (não está contido)
'''


#Exemplos

b = 2 > 4 and 2 == 4
c = 2 > 4 or 2 < 4
d = not(2 > 4 or 2 < 4)
e = not(2 > 4 and 2 == 4)

string = "Babaca é o seu pai"

print('b' in string) #a letra 'b' está na variável 'string'? Verdadeiro
print('C' in string) #a letra 'C' está na variável 'string'? Falso
print('d' not in string) #a letra 'd' não está na variável 'string'? Verdadeiro

print(2 is 2) #2 é 2? Verdadeiro
print(3 is 2) #2 é 3? Falso
print(type(1)) #Qual o tipo do objeto '1'? Inteiro
print(type(1) is int) #O tipo do objeto '1' é inteiro? Sim
print(type(1) is not float) #O tipo do objeto '1' não é um ponto flutuante? Sim
