altura=float(input("informe o valor da altura do cone:"))
raio=float(input("Infomre o valor do raio do cone: "))

pi=3.14

area_base=(pi*raio)**2

lado_inclinado=((altura**2 + raio**2 )**1/2)


area_superfi_lateral= pi*raio*lado_inclinado

area_total=area_base + area_superfi_lateral

print(f"Área total é {area_total}")




           