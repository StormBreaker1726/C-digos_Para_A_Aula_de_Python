#Atribuição Múltipla

'''
É a capacidade de atribuir um conjunto de valores a um conjunto de variáveis
'''

#Exemplo

a = 10
b = 5

'''
E se precisassemos "inverter" os valores das variáveis? Ou seja, fazer a = 5
e b = 10
Para fazer isso, seguimos o comando abaixo:
'''
a, b = b, a #Faz com que o valor de a passe para b, e b passe para a
print(a); print(b)

#Analogamente, podemos fazer isso com mais de 2 variáveis:

a = 1
b = 2
c = 3
d = 4

print("VALORES ANTERIORES")
print(a); print(b); print(c); print(d)

a, b, c , d = d, c, b, a

print("VALORES NOVOS")
print(a); print(b); print(c); print(d)

#Podemos também usar esse processo para atribuir valores à variáveis:
#Exemplo:
x, y = 2, 5
print(x); print(y)
#Resumindo.....
'''
Sempre que temos a expressão x, y = valor1, valor2, x irá receber o valor1, e
y irá receber o valor2. Ou seja, a primeira variável recebe o primeiro valor
e a segunda variável recebe o segundo valor. Podemos usar o mesmo processo para
atribuir strings à variáveis também
'''
#Exemplo aplicado:
'''
Tendo as variáveis a, b & c, associe uma operação matemática a cada uma das
variáveis
'''
a, b, c = 2, 4, 8 #declarando as variáveis e associando um valor inicial nelas
a, b, c = a**2, a+b+c, a*b*c #atribuindo as operações
print(a); print(b); print(c)

'''
#Vale lembrar que as operações matemáticas foram processadas ao mesmo tempo,
ou seja, ao atribuir um novo valor para 'a' na primeira operação, ele não será
considerado na segunda operação, e só mudará no termino do processamento de 
todas as operações. 
'''