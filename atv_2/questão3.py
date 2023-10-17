senha_padrao = "swordfish"
erro = 0

while True:
    senha_pessoal = input("Digite a senha: ")
    erro += 1

    if senha_pessoal == senha_padrao:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")

print(f"A senha está correta! os números de  tentativas. {erro}")
