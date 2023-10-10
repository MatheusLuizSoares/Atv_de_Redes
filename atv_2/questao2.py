

n = int(input("Digte  um número: "))
res = 1

print(f"Fatorial de {n}:")
while n > 1:
    res *= n
    n -= 1
    print(res, end=' ')

print("Divisores do fatorial:")
divisao = 1
while divisao <= res:
    if res % divisao == 0:
        print(divisao, end=' ')
    divisao += 1