#Instrução Continue:
'''
É a instrução que interrompe a execução de apenas um ciclo, porém, não termina a execução do
laço completamente
'''
for i in range(10):
    if(True):
        continue

i = 10
while (i < 100):
    i += 1
    if(True):
        continue

#Exemplo na prática:
print("")
print("início")

i = 0
while(i < 10):
    i += 1
    if(i % 2 == 0):
        continue            #Quando invocamos essa função apenas pulamos o bloco if, não todo o bloco de repetição
    print(i)
else:
    print("else")
print("")
print("fim")

#Indo mais a fundo no programa anterior:
i = 0
while(i < 10):
    i += 1
    if(i % 2 == 0):
        continue            #Quando invocamos essa função apenas pulamos o bloco if, não todo o bloco de repetição
    if(i > 5):
        break               #Aqui, por exemplo, utilizamos o break quando o i for maior que 5, e isso não deixará que o else seja executado 
    print(i)
else:
    print("else")
print("")
print("fim")
