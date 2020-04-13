#Blocos de Instrução parte II:

'''
Blocos de instrução garantem mais segurança para o programa. Por exemplo, variáveis
declaradas dentro de um bloco de instrução só podem ser acessadas dentro deste mesmo
bloco de instrução (se declararmos uma varíavel dentro de um if, por exemplo, não
podemos fazer referência dela fora do bloco de instrução do if; já se declararmos
a variável no escopo global, podemos manipulá-la em qualquer parte do programa
'''

'''
No python é extremamente importante que respeitemos o espaçamento (identação) dos
blocos de instrução
'''

'''
Podemos ter um bloco de instrução dentro do outro, se for necessário
'''
'''
No caso da IDE utilizada (VSCode), eu utilizo uma extensão que me permite colorir as identações dos diversos
BIs para não me confundir
'''
a = 25

if(True): #primeiro if
    a = 50 #comando dentro do BI do primeiro if
    if(False): #segundo if; comando dentro do BI do primeiro if
        b = 50 #comando dentro do BI do primeiro e segundo if
    a = 40 #comando dentro do BI apenas do primeiro if