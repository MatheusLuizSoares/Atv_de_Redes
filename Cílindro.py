
raio=float(input("Informe o raio do cílindro:"))
altura=float(input("Altura do cílindro:"))
pi=3.14

Area_lateral=float( 2*pi*raio*altura)

Area_base=pi* raio**2

area_total=((2*pi)*raio**2)+2*pi*raio*altura
print(f"área total é {area_total:.4f}")