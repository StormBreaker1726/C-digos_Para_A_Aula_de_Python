#escopo:
'''
São as regiões onde uma variável pode ser declarada e usada.
'''
#variáveis em escopo global
a = 1 
b = 2

def soma_num(var1, var2):
    #escopo local da função soma_num
    s = var1 + var2
    return s

def imprime(x_vezes):
    #escopo local da função imprime
    for i in range(x_vezes):
        print(i)

print(soma_num(a, b))
imprime(5)
