
a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

delta = (b**2) - 4*a*c
if delta >= 0:
    var1 = (-b + delta**0.5) / (2*a)
    var2 = (-b - delta**0.5) / (2*a)
    print(f"O valor da  variavel um é {var1:.2f} e o valor da variavel dois é {var2:.2f}")
else:
    print("A equação não possui raízes reais.")
