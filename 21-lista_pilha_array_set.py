#Lista, Pilha, Array, Set

'''
Pilha:
    1) É um conjunto de elementos adicionados um sobre o outro
    2) O último elemento a entrar será o primeiro a sair
    3) O primeiro elemento a entrar será o último da lista
    Para facilitar a vizualisação desses conceitos, imagine uma pilha de livros:
        você pegará o primeiro e colocará sobre a mesa; o segundo irá sobre o 
        primeiro, o terceiro sobre o segundo e assim por diante. O último livro
        que você colocará na mesa será o primeiro a sair, e o primeiro que você
        colocou sobre a mesa é o último na pilha.
    
    Diferença entre a pilha e a lista: na lista os elementos que vão sendo adicionados
    vão para o fim da lista. Na pilha ocorre o exato oposto: os elementos que vão sendo
    adicionados vão se tornando os primeiros elementos da pilha (os primeiros a serem
    lidos).
    
Array (vetores) - não muito utilizadas no Python:
    1) É um conjunto de elementos finitos, de um único tipo e definidos na sua 
    declaração, ou seja, não conseguimos adicionar ou excluir elementos no array 
    durante a execução do programa.
    2) O índice 0 é o primeiro elemento da lista
    3) O índice do último elemento é o "total_de_itens-1"
    
    array[tamanho(quantidade de elementos + 1)] = {elementos}
    
Tupla (read-only):
    1) É uma lista declarada como uma constante
    2) Não é possível adicionar, remover ou alterar elementos
    3) Toda tupla será um conjunto de objetos também imutáveis, mas que não precisam ser
    de mesmo tipo
    
    Na declaração, devemos fornecer:
        a) Quantos elementos terá na tupla
        b) Quais serão esses elementos

Set:
    1) Estrutura de dados semelhante a uma lista, ou seja, podem ser alterados
    2) Tem como princípio conter uma lista de valores diferentes
    3) É uma lista sem itens repetidos
    
Dicionário:
    Estrutura na qual cada item possui uma chave única e que pode ser 
    de qualquer tipo. Será trabalhado mais pra frente.

Árvores:
    1) Raíz - elemento pertencente ao nível zero. Toda árvore terá sempre uma única
    raiz
    2) Nó/Filho - elemento que foi adicionado a outro item. Cada nó que tiver 
    um filho, tem uma sub-árvore, ou seja, é um ramo da árvore maior
    3) Nível - propriedade que indica quantos nós estão acima de um filho
    
    Pode ser usado para cadastrar informações de maneira pré-organizada. Pesquisa
    extremamente fácil.

    
'''