#operadores relacionais:
#são utilizados para verificar condições e julgarem se verdadeiro ou falso

b = (3>2) 
'''
no que a variável b checa a condição dada entre parênteses ela irá 
retornar true ou false. Sendo assim, ela passa a ser uma variável do tipo 
boolean ou também chamada de variável bool
'''
c = (2<3) # c tb é uma bool

if(c==True):
    print("Verdadeiro")
else:
    print("Falso")

#operadores

'''
Maior que:	>
Menor que:	<
Igual a:	==
Maior ou igual a:	>=
Menor ou igual a:	<=
Ou: |
Identidade(algo é outra coisa): is
Identidade(algo não é outra coisa): is not
Diferente de: !=

para uma lista maior de operadores ir em:
https://docs.python.org/3/library/operator.html#mapping-operators-to-functions

podemos utilizar os operadores tb para comparar lugar de caracteries na tabela ASCII
'''
print('a'>'A') #na tabela ASCII o caracterie A se encontra na posição 65,
#enquanto o a se encontra na posição 97