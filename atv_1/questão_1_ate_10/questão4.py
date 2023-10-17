#Faça um programa que leia um valor inteiro correspondente a um ano e diga se o ano informado é bissexto ou não.

ano=int(input("Digite o ano:"))

if  ano % 4 == 0:
    print("ele é ano bissexto")
elif ano % 100 != 0 and ano % 400 == 0:
  print("ele é ano bissexto")
else:
  print("Ele não é ano bissexto")
