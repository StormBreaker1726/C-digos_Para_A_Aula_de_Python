#Potenciação e Radiciação
#para potenciação utilizamos o operador **
#Exemplo:

print(7**2)

#Exemplo aplicado:
base = float(input("Digite a base:"))
expoente = float(input("Digite o expoente:"))

result = base**expoente

print(result)

#para radiciação usamos:
#base**(1/expoente). Ex:
#Raiz de 81

print(81**(1/2))

#Exemplo aplicado:
base = float(input("Digite o número que deseja obter a raíz:"))
expoente = float(input("Digite o expoente da raíz:"))

result = base**(1/expoente)

print(result)

#Existe uma biblioteca que já vem com definições para radiciação e potenciação
#para inclui-la usamos o comando--> import math
#para saber oq ela pode fazer, digitamos--> print(dir(math))
#para utilizar alguma função dela--> math.função_desejada