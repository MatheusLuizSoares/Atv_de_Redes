
valor=int(input("Digite um valor:"))

a=0
b=1
print("A sequência de Fibonacci são:", end=" ")

calc = 0
while calc < valor:
        print(a, end=" , ")
        a,b=b,a+b
        calc += 1