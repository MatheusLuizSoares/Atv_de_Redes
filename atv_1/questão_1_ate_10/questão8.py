
valor = float(input("Digite o valor do saque: "))

if valor <= 0:
    print("Valor inválido. Digite um valor positivo.")
else:
    centavos= int(valor * 100)

    if centavos >= 10000:
        cedulas100 = centavos // 10000
        centavos %= 10000
        print(f"Cédulas de R$ 100,00: {cedulas100}")

    if centavos >= 5000:
        cedulas50 = centavos // 5000
        centavos %= 5000
        print(f"Cédulas de R$ 50,00: {cedulas50}")

    if centavos >= 2000:
        cedulas20 = centavos // 2000
        centavos %= 2000
        print(f"Cédulas de R$ 20,00: {cedulas20}")

    if centavos >= 1000:
        cedulas10 = centavos // 1000
        centavos %= 1000
        print(f"Cédulas de R$ 10,00: {cedulas10}")

    if centavos >= 500:
        cedulas5 = centavos // 500
        centavos %= 500
        print(f"Cédulas de R$ 5,00: {cedulas5}")

    if centavos >= 200:
        cedulas2 = centavos // 200
        centavos %= 200
        print(f"Cédulas de R$ 2,00: {cedulas2}")

    if centavos >= 100:
        moedas1 = centavos // 100
        centavos %= 100
        print(f"Moedas de R$ 1,00: {moedas1}")

    if centavos >= 50:
        moedas050 = centavos // 50
        centavos %= 50
        print(f"Moedas de R$ 0,50: {moedas050}")

    if centavos >= 25:
        moedas025 = centavos // 25
        centavos %= 25
        print(f"Moedas de R$ 0,25: {moedas025}")

    if centavos >= 10:
        moedas010 = centavos // 10
        centavos %= 10
        print(f"Moedas de R$ 0,10: {moedas010}")

    if centavos >= 5:
        moedas005 = centavos // 5
        centavos %= 5
        print(f"Moedas de R$ 0,05: {moedas005}")

    if centavos >= 1:
        moedas001 = centavos
        print(f"Moedas de R$ 0,01: {moedas001}")
