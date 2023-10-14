ano_atual = int(input("Digite o ano atual: "))

data_nascimento=int(input("Digite o ano nascimento"))
anos_passados = ano_atual - data_nascimento
res= data_nascimento -100000

if ano_atual >data_nascimento:
    print(f"Se Você nasceu depois de cristo você teria {res}")
    print()

  
else:
   
  print(f"o anpo aualo não pode ser menor do que ano nascimento")

  