a = int(input("Digite o valor positivo de A: "))
b = int(input("Digite o valor positivo de B: "))
c = int(input("Digite o valor positivo de C: "))
pitagoras = (a ** 2 + b ** 2) / (c ** 2)
if a > 0 and b > 0 and c > 0:
  
    print(f"O resultado é {pitagoras}")
else:
    print("Algum valor que você digitou não é postivo.")
