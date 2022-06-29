#TESTA SE UM NÚMERO FAZ PARTE DA SEQUÊNCIA DE FIBONACCI
fibo = 0
aux = 1
lista_fibo = []
temp = 0
numero = int(input("Digite um numero: "))
teste = True
while fibo <= numero:
    lista_fibo.append(fibo)
    fibo = fibo + aux
    aux = lista_fibo[temp]
    temp = temp + 1
    if (fibo == numero):
        print(f"O número {numero} faz parte da sequência de Fibonacci")
        teste = False
if(teste):
    print(f"O número {numero} não faz parte da sequência de Fibonacci") 
print(lista_fibo)
