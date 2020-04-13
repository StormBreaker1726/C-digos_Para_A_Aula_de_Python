#Iterando listas:

lista_nums = [100, 200, 300, 400]

for item in lista_nums: #imprimirá cada elemento da lista e atribuirá a item o valor do elemento
    print(item)
    
lista_indice = [0, 1, 2, 3]

for item in lista_indice: #irá alterar o valor da lista_nums adicionando 1000 em cada um dos elementos
    lista_nums[item] += 1000
print(lista_nums)

#Função range:
lista = list(range(0,4)) #irá gerar uma lista com 4 elementos a apartir da posição 0

lista_nums = [100, 200, 300, 400]

for item in range(len(lista_nums)): #irá alterar o valor da lista_nums adicionando 1000 em cada um dos elementos
    lista_nums[item] += 1000
print(lista_nums)

#Função enumerate:

lista_nums = [100, 200, 300, 400]

for idx,  item in enumerate(lista_nums) :
    lista_nums[idx] += 1000 
print(lista_nums)

