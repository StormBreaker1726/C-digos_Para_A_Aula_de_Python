#Class List I

#Trabalhando com Listas na prática

'''
Maneiras de declarar uma lista no Python:
'''
lista01 = [1, 2, 8, 5 ,15, 3, 6, 8]; print(lista01)
lista02 = ["João Víctor", "Costa de Oliveira"]; print(lista02)

print(type(lista01), type(lista02)) #saída deverá indicar que as variáveis são do tipo lista


#Retornando elementos da lista
'''
nome_da_lista[índice_do_elemento]
'''
print(lista01[2]) #retornará o elemento na posição 2 (o 3º elemento da lista)

#Operações com elementos de listas
'''
Podemos fazer operações matemáticas com elementos de listas. Exemplo:
'''

lista01 = [0.2, 5, 5, 8, 9, 0]
lista02 = [4, 5, 4, 2, 0, 0]

print(lista01[0] + lista02[0]) #retorna a soma dos valores contidos na posição referenciada de cada lista

l = ["a", "b", "c", "d", "e", "f"]
z = ["g", "h", "i", "j", "k", "l"]

print(l[2] + z[2]) #concatena sem espaço as duas strings contidas na posição referenciada em cada lista

print(l[2] + " " + z[2]) #concatena com espaço as duas strings contidas na posição referenciada em cada lista

#Podemos declarar uma lista dessa maneira também:

lista = list("João Víctor Costa de Oliveira")

print(lista) #deverá imprimir cada uma das sub-strings digitadas, incluindo os espaços

lista03 = list("123456789")

print(lista03)

#Cada elemento se transforma em um elemento da lista

#Também podemos fazer assim:
lista_mae = [2, 3, 4, 5]

lista04 = list(lista_mae) #faz com que todos os elementos da lista_mae se transformem em elementos da lista04

print(lista04) #imprime os elementos da lista04

#É comum deixar uma vírgula no final de cada lista ou de uma tupla:
'''
a = (5)--> interpretado como objeto numérico
a = (5,)--> interpretado como lista
'''
#Brincando com listas:

notas_prova1 = [2, 5, 4, 0, 3]
notas_prova2 = [5, 0, 4.5, 0, 0]
notas_finais = [0, 0, 0, 0, 0]

for i in range(5):
    if(notas_prova1[i]>notas_prova2[i]):
        notas_finais[i] = notas_prova1[i]
    elif(notas_prova1[i]<notas_prova2[i]):
        notas_finais[i] = notas_prova2[i]
    elif(notas_prova2[i] == notas_prova1[i]):
        notas_finais[i] = notas_prova1[i]

print(notas_finais)
