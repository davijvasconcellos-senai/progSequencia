nome = input("Digite o seu primeiro nome:")
idade = int(input("Digite sua idade:"))

# print("Olá,", nome, "!")
# print("Tudo bem com você?")
# print("Caramba", nome, "! você tem", idade, "anos? Nem parece.")

print("Olá, {}!".format(nome))
print("Tudo bem com você?")
print("Caramba {}! você tem {} anos? nem parece.".format(nome, idade))

nome = "Davi"
print(f"Meu nome é {nome}.")
print(f"Meu nome é {nome.lower()}.")
