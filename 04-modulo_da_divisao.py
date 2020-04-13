#módulo da divisão:
#utilizado quando queremos saber o "resto" da divisão

print(10%6)
print(6%2)

print(900%2 == 0)
print(900%7 == 0)

#exemplo em programa:
num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))

rest = (num1%num2) #retorna o módulo da divisão
resul = (num1//num2) #retorna a parte inteira da divisão
resul_cert = (num1/num2) #retorna o resultado real (com ponto flutuante) da divisão

print(rest)
print(resul)
print(resul_cert)
