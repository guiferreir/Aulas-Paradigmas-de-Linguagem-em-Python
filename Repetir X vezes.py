# Leia um inteiro X e imprima X vezes a mensagem "NepsAcademy eh Sucesso".

x = int(input("Digite um número inteiro entre 1 e 100: "))

# Verifica se o número está dentro das restrições
if 1 <= x <= 100:
    for _ in range(x):
        print("NepsAcademy eh Sucesso")
else:
    print("Erro: O número deve estar entre 1 e 100.")