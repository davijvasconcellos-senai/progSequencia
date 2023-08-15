#Criando var nome, exibindo mensagem na tela e fazendo entrada de dados do teclado, salavando na var nome
nome = input("Informe o seu nome:")
print("Nome inserido:", nome) #Exibindo conteúdo da var nome

'''
Repetindo a ação anterior,
só que desta vez,
com uma var do tipo int
'''
numero = int(input("Digite um número"))
print("Número inserido:", numero)

salario = float(input("Informe o seu salário: "))
print("Seu salário é R$ ", salario)

print("Tipo da var nome: ", type(nome))
print("Tipo da var numero:",type(numero))
print("Tipo da var salario:",type(salario))

nome2 = "Davi"
numero2 = 10
salario2 = 3456.78

print("Nome2:", nome2)
print("Número2:", numero2)
print("Salário2 ", salario2)

print("Tipo da var nome2: ", type(nome2))
print("Tipo da var numero2:",type(numero2))
print("Tipo da var salario2:",type(salario2))
