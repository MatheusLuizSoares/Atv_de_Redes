coord1x = float(input("Digite a coordenada x do primeiro ponto:"))
coord1y = float(input("Digite a coordenada y do primeiro ponto:"))
coord2x = float(input("Digite a coordenada x do segundo ponto:"))
coord2y = float(input("Digite a coordenada y do segundo ponto:"))

distancia = ((coord2x - coord1x) ** 2 + (coord2y - coord1y) ** 2) ** 0.5

print(f"A distância entre os pontos ({coord1x}, {coord1y}) e ({coord2x}, {coord2y}) é {distancia}")
