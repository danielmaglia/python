#PROGRAMA
senha = 0
contin = "s"
while contin == "s":
    name = str(input("Digite seu nome completo: "))
    years = int(input("Digite a idade: "))
    if years <=12 and years >= 5:
        exam = int(input("Digite a area da ressonancia magnétic, 1= BACIA, 2=CRANIO 3=TORAX: "))
    if exam == 1:
         print("O seu exame é de Bacia")
    elif exam == 2:
         print("O seu exame é de Crânio")
    elif exam == 3:
         print(" O seu exame é de Torax")
    else:
         print("Número Inválido")
#
    senha += 1 
    if senha >1000:
         print("Excedeu o limite de atendimentos")
    else:
         print (" a senha de atendimento é", senha)
         contin = str(input("deseja continuar? "))
else:
    print("Não atendemos") 

    