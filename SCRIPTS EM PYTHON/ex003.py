#Exercício 3
n = int(input("Digite a quantidade de números pares que deseja: "))
cont = 0
par = 0
while cont < n:
    if par % 2 == 0: 
        print(par) 
        cont += 1 
    par += 1