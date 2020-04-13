#Instrução Break:
'''
É a instrução que interrompe a execução do laço de repetição
na qual está contida
Toda vez que podemos interromper um laço de repetição, devemos interromper,
pois ao fazer isso podemos economizar recursso do computador e fazemos com
que nossa aplicação fique ainda mais rápida
'''

#Exemplo da Instrução "break" sendo utilizada:

for i in range(10):
    if(True):
        break

#Exemplo prático:

for f in range(10):
    if(f % 2 != 2):
        print("Hello")
    else:
        break

#Exemplo prático 2:
i = 10
while(1 < 100):
    i += 1
    if(i / 2 == 5.5):
        break

#Exemplo prático 3:
print("Antes de entrar no laço")
for item in range(10):
    print(item)
    if(item == 6):
        break

