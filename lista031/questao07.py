"""
Fazer um algoritimo que pergunte 3 números e apresente a média
aritmética entre estes 3 números.
"""

n1 = float(input("Informe um número: "))
n2 = float(input("Informe um outro número: "))
n3 = float(input("Informe outro número: "))

media = (n1 + n2 + n3) / 3

print("A média entre estes 3 números é: {:.2f}".format(media))