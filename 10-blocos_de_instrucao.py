#Bloco de Instruções

'''
É um conjunto de instruções que se encontram no mesmo nível de identação,
mesmo nível hierárquico
'''
if(True):
    print("Imprima um texto")
    print("Imprima um texto")
    print("Imprima um texto")
    print("Imprima um texto")

if(False):
    print("Não imprima um texto")
    print("Não imprima um texto")
    print("Não imprima um texto")

'''
Podemos dizer que o if pode alterar a ordem de execução dos blocos de instrução
já que (usando o caso acima como exemplo) só executaremos as linhas 8 à 11
se a condição descrita na linha 7 for verdadeira. Caso contrário, ele não
executará.
'''
