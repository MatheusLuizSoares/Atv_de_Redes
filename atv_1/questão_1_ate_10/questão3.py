#impar positivo impar negativo


numero=int(input("Digite um número:"))
resto= numero %2
negativo= numero<0 


if negativo %2:
    print("Ele é negativo par")
elif numero==0:
    print("Ele é nulo")
elif negativo ==1:
    print("Ele é negativo impar")

elif resto ==0:
    print("Ele é número par ")
elif resto ==1:
    print("Ele é o número impar")


