#Class List II:

'''
Como já dito anteriormente, em uma lista podemos ter todos os tipos de elementos, inclusive outras
listas. Também podemos ter uma lista que contém elementos de tipos diferentes dentro delas.
Ex: lista01 = ['nome', 3]
Podemos ter listas contendo listas:
Ex: lista = [[list1],[list2],[list3]]
Nesse caso se utilizarmos o comando lista[0] (para saber o elemto na posição 0 da lista chamada
lista), teremos como retorno uma outra lista: [list1].
Para acessarmos um elemento de uma sublista, podemos utilizar o comando: 
    lista[posiçao da lista][posiçao da sublista]
Segue o exemplo:
'''
lista_a = [['bacalhau ', 'pirarucú ','sardinha '],[1, 25, 35],['R$25,00', 'R$30,00', 'R$5,00']]
print(lista_a[0][2])
print(lista_a[0][0] + lista_a[2][0])

'''
No Python, se quisermos retornar o valor do último elemento da nossa lista, podemos utilizar o comando:
nome_da_lista[-1]
Segue o exemplo:
'''
print(lista_a[-1])

#Funções/métodos que poderemos usar com qualquer lista no Python:

'''
1) len --> retorna o tamanho da lista (quantos elementos) *Não é o mesmo que o índice do último 
elemento da lista

2) nome_da_lista = nome_da_lista + [elemento] --> adiciona o elemento no final da 
lista selecionada *Podemos adicionar quantos elementos quisermos [][][]... *concatenação de lista

3) nome_da_lista = [elemento] + nome_da_lista --> adiciona o elemento no início da 
lista selecionada *Podemos adicionar quantos elementos quisermos [][][]... *concatenação de lista

4) nome_da_lista.append(elemento) --> tb adiciona um elemento no final da lista selecionada *coloca
o elemento

5) del(nome_da_lista[posicao_do_elemento]) --> exclui o elemento na posição selecionada da lista
selecionada

6) nome_da_lista = nome_da_lista + numero_de_vezes*[elemento] --> add o elemento um determinado
número de vezes na lista selecionada *Podemos fazer o equivalente para add no início

Obs: podemos utilizar um jeito parecido para gerar elementos do mesmo tipo um determinado número
de vezes na tela. Por exemplo, se fizermos print(50*"-"), o - aparecerá 50 vezes na tela 
do programa

'''

'''
ATENÇÃO: TODOS OS COMANDO A SEGUIR DEVEM SER COLOCADOS DA SEGUINTE MANEIRA--> nome_da_lista.comando

1) append(x) --> acrescenta item x ao final da lista

2) copy() --> cópia superficial

3) extend(L) --> acrescenta a lista L ao final da lista

4) insert(x,y) --> insere y após o item na posição x

5) remove(x) --> remove o valor x

6) sort() --> ordena a lista crescentemente 

7) clear() --> limpa a lista

8) count(x) --> retorna a quantidade de ocorrências de x

9) index(x) --> retorna o primeiro índice correspondente ao valor x

10) pop(x) --> remove item de índice x *se deixarmos o () em branco, excluímos o último

11) reverse() --> inverte a ordem da lista *sort(reverse = True)



'''


