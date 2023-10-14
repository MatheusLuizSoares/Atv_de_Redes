
A=float(input("Digite um número Positivo do cateto:"))
B=float(input("Digite um segundo número do positivo do cateto:"))
C=(input("Digite  o valor da hipotenusa:"))
hipotenusa= (A**2 + B**2) **(1/2)
if A>0 and B>0:
  print(f"O valor da hipotenusa é {hipotenusa}")
else:
  print("O valor não pode ser negativo")