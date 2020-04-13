#Fatiando listas: extrair listas de outras listas

'''
Todas as listas tem índices positivos e negativos. Os índices positivos são os que normalmente
tabalhamos. Os índices negativos começam do -1 (último elemento) e vão até o -(número de itens).
Por exemplo: lista = ['P', 'Y', 'T', 'H', 'O', 'N'], a lista a seguir tem índices de 0 a 5 e
-1 a -6.

0 ou -1 : N
1 ou -2 : O
2 ou -3 : H
3 ou -4 : T
4 ou -5 : Y
5 ou -6 : P
'''

'''
Para fatiarmos a lista usaremos a seguinte estrutura:
    lista_nova = lista_velha[x:y:z]
    x--> de onde começar (start) *Sem definição = 0
    y--> até onde vai (stop) *Sem definição = len()
    z--> de quantos em quantos (passo ou step) *Sem definição = 1
'''
lista_velha = ['P', 'Y', 'T', 'H', 'O', 'N']

lista_nova = lista_velha[::2]

'''
Como alternativa ao comando reverse() podemos utilizar a estrutura lista[::-1] para reverter a lista
'''

#Brincando com essas listas

frase_original = "anotaramadatadamaratona"
frase_reversa = frase_original[::-1]

lista = "joao victor costa de oliveira"

l = lista[:20] #l irá receber as posições de 0 até 20 da lista chamada lista

k = lista[2:20] #k irá receber as posições de 2 até 20 da lista chamada lista