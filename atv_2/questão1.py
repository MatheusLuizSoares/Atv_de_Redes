continuo = 'S'

while continuo == 'S' or continuo == 's':
    valor_mensal = float(input("Informe o valor mensal a ser aplicado (R$): "))
    taxa_mensal = float(input("Informe a taxa de juros mensal (%): "))

    valor_acumulado = 0
    meses = 0

    while meses < 12:  
        valor_acumulado += valor_mensal
        valor_acumulado += valor_acumulado * (taxa_mensal / 100)
        meses += 1

    print(f"O valor acumulado do primeiro ano é (R$): {valor_acumulado:.2f}")

    continuo = input("Deseja calcular mais um ano S OU N ")
