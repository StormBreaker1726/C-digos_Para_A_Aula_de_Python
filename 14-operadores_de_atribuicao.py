#operadores de atribuição
'''
O valor que está no lado direito do operador é atribuído à variável a esquerda
do operador
'''

'''
x = y #x recebe y
x == y #x igual a y
'''

#Exemplo:

x = z =7 #atribui a x e z o mesmo valor
y = 4

a = (x == y) #checará a proposição no parênteses
print(a) 

b = (x == z) #checará a proposição no parênteses

print(b)

'''
Operadores de atribuição
'''

'''
Acrescentar unidade à variável (utilização no while): x += unidade
'''
#Exemplo:

x = 1
print(x)

x += 1
print(x)

x += 2
print(x)

'''
Se temos as variáveis x = 3 e y=2, podemos:
---> Subtrair x de y: x -= y
---> Dividir x por y: x /= y;
---> Multiplicar x por y: x *= y
--- Saber o resto (ou o módulo) de x por y: x %= y
'''

x = 9
y = 3

x -= y; print(x)

x *= y; print(x)

x /= y; print(x)

x %= y; print(x)
