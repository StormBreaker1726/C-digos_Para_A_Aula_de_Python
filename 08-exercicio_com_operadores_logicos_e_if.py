#Exercicio com operadores lógicos e if

#Utilizei if em td pq se não ele pararia na primeira condição que estivesse certa

numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))

if(numero1 == numero2):
    print("O número %.2f é igual ao número %.2f"%(numero1, numero2))
if(numero1 != numero2):
    print("O número %.2f é diferente do número %.2f"%(numero1, numero2))
if(numero1 < numero2):
    print("O número %.2f é menor que o número %.2f"%(numero1,numero2))
if(numero1 > numero2):
    print("O número %.2f é menor que o número %.2f"%(numero1, numero2))
else:
    print()
