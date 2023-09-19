nota1=float(input("Digite a sua nota:"))
nota2=float(input("Digite a sua segunda nota:"))
media= (nota1*2 + nota2*3)/5
print(f"A sua nota final é: {media}")

if media>=60:

    print("Voce está aprovado")

elif media>20:
    print("Voce está recuperação ")


else:
  print("voce foi reprovado")
 
