qtd_amigos = int(input("Digite a quantidade de amigos: "))
pizza = qtd_amigos // 8

if qtd_amigos % 8 == 0:
    print(pizza)
else:
    print(pizza + 1)