qtd_amigos = int(input("Digite a quantidade de amigos: "))
pizza = qtd_amigos // 8 # o "//" é uma divisao inteira

# Quando a divisao for exata
# Quando a divisao nao for exata

if qtd_amigos % 8 == 0:
    print(pizza)
else:
    print(pizza + 1)