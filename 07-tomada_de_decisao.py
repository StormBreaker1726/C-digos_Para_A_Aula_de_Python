#tomada de decisões:

#instrução if: mesma tomada de decisão que no C. Sintaxe:
#if(condição a ser checada):
    #comando a ser executado
#elif(condição a ser checada):       ---> isso pode ser usado quando devemos checar várias condições
    #comando a ser executado              
#else:
    #comando a ser executado se a condição não for verdadeira

#Exemplo prático:

a = float(input("Digite um número:"))

if(a == 12):
    print("Acertou")
elif(a == 11):
    print("Quase lá")
else:
    print("Errou!!!")

acao = int(input("Digite '1' para sim e digite '2' para não:"))

if(acao == 1):
    print("Você disse que sim")
else:
    if(acao == 2):
        print("Você disse que não")
    else:
        print("O número digitado é inválido")
    