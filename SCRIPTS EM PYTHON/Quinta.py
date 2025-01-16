sal = float(input("Digite seu salário: "))

if sal <= 2500.00:
    new = sal * 1.15
elif sal <= 4999.00:
    new = sal * 1.10
else:
    new = sal * 1.05

print("O novo salário será: ", new)