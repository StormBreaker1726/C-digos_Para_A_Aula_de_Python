#Iteração
'''
Laços condicionais - Looping - Controle de Fluxo:
    É o processo de repetição na qual um bloco de instrução é executado enquanto uma
    determinada condição for atendida
    Utilizada para evitar repetição de códigos sem necessidades
'''
'''
Os tipos de controle de fluxo no Python são:
    for --> utilizado para executar um bloco de comando uma determinada quantidade
de vezes
    while --> utilizada para executar um bloco de comando até que uma determinada condição
pare de ser atendida
'''
'''
Obs.: diferentemente do C, no Python NÃO precisamos mandar a variável-de-controle se
atualizar/complementar. Ela fará isso SOZINHA. No while PRECISAMOS atualizá-la
'''
#Exemplo prático:
x = 0
while (x <= 10 ):
    print(x); x+=1
    #Lembrete--> x irá valer 11 no final desse looping, porém só irá imprimir até o valor 10

'''
Para utilizar a função for, precisamos utilizar a função range() junto. Segue o exemplo
'''
b = 0
for b in range(5):
    print(b)

'''
Podemos utilizar tb uma estrutura especial do Python, chamada while-else. Ela executará
o bloco do while; no momento em que parar de executá-lo, executará o bloco do else.
Segue o exemplo:
'''
c = 0
while(c <= 10):
    print(c); c += 1
else:
    print("Acabou a contagem")

'''
Podemos também utilizar o for para imprimir valores em uma lista genérica seguindo a estrutura:
    for <var> in list:
        comando
Segue o exemplo:
'''
for g in "joao victor":
    print(g)