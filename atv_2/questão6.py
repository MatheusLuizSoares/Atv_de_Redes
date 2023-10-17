valor = input("Informe um valor inteiro: ")

contador = 0
posicao = 0


while valor[posicao:posicao + 1]:
    letras = valor[posicao]
    if letras >= '0' and letras <= '9':
        contador += 1

    posicao += 1

print(f"O valor informado possui {contador} dígito(s).")
