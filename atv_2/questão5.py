n = int(input("Digite algum número positivo: "))

divisor = 2  

while divisor <= n:
    if n % divisor == 0:
        print(f"{divisor} é divisor de {n}")
    divisor += 1

if divisor == n + 1:
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
