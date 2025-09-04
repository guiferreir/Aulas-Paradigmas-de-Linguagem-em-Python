n = int(input())

if 0 <= n <= 12:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(fatorial)