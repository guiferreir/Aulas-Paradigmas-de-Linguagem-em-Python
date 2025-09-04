a = int(input("Digite o primeiro número (A): "))
b = int(input("Digite o segundo número (B): "))

if -100 <= a <= 100 and -100 <= b <= 100:
    menor = min(a, b)
    maior = max(a, b)
    
    for i in range(menor, maior + 1):
        print(i, end=" ")