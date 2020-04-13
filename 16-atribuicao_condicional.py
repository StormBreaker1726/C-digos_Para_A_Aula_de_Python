#Atribuição Condicional

'''
É uma estrutura utilizada para simplificar o código, cujo valor a ser atribuído
será aquele que satisfazer a condição
'''

#Estrutura básica de uma atribuição condicional:

'''
<variavel> = <valor1> if(True) else <valor2>
'''
#Exemplo:

var = 10 if(True) else 20

#Meu exemplo 1:
i = 0

for i in range(10):
    i = i if(i % 2 == 0) else (0//i)
    print(i)

#Meu exemplo 2:

x = 0
for x in range(10):
    texto = "par" if (x % 2 == 0) else "ímpar"
    print("O número %d é: "%x + texto) 

#Melhorando meu exemplo 2:

x = int(input("Digite um número: "))

numero = "par" if(x % 2 == 0) else("ímpar")
print("O número %d é: " %x + numero)