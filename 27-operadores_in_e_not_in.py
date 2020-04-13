#Operadores in e not in:
'''
São operadores que verificam se o operando a esquerda está ou não contido na lista a direita

x in [...] #verifica se o valor de x está na lista (True ou False)
x in (...) #verifica se o valor de x está na tupla (True ou False)

x not in [...] #verifica se o valor de x não está na lista (True ou False)
x not in (...) #verifica se o valor de x não está na tupla (True ou False)
'''

resp = 2 in (0,1,2,3,4,5,6,7,8,9,10) #resp deverá assumir o valor booleano de True

resp01 = 11 in (0,1,2,3,4,5,6,7,8,9,10) #resp01 deverá assumir o valor booleano de False

resp02 = 11 not in (0,1,2,3,4,5,6,7,8,9,10) #resp01 deverá assumir o valor booleano de True