#Blocos de Instrução-Prática:

n1 = int(input("Digite um numero:"))

if(n1 > 10):
    print("O valor é maior que 10!!!")
    if(n1 < 15):
        print("O valor é maior doq 10, mas menor doq 15")
    else:
        if(n1 == 50):
            print("O valor é 50!!!")
        else:
            if(n1 < 50):
                print("O valor é maior doq 10 porém menor que 50")
            else:
                print("O valor é maior doq 50")
else:
    if(n1 > 5):
        print("O número é maior doq 5 mas menor que 10")
        if(n1 == 5):
            print("O número é igual a 5")
        if(n1 == 7):
            print("O núemero é igual a sete")
    else:
        print("O valor é menor doq 5")