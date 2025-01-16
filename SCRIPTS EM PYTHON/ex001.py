#EXERCÍCIO 1
num1= float(input("Digite um número: "))
opera= (input("Digite o operador desejado: "))
num2= float(input("Digite um número: "))
if opera == "+":
    resul= num1+num2
elif opera == "-":
    resul = num1-num2
elif opera == '*':
    resul= num1*num2
elif opera == '/':
    resul= num1/num2
else:
    print ('número inválido')
print(f" O {num1}{opera}{num2}={resul}")
