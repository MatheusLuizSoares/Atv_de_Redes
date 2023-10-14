

Vendedor=str(input("Digite o nome do vendedor:"))
salario_fixo=float(input("Digite o salario fixo do Vendedor:"))
venda=int(input("Digite a quantidade de dinheiro que ele recebeu por venda no mês:"))

salario_final= salario_fixo+(0.15*venda)
print(f"O salario final de {Vendedor} é {salario_final:.2f} ")
