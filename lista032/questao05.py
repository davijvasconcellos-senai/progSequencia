"""
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois números,
a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a multiplicação entre
dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão do primeiro pelo segundo número.
"""

n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe um segundo número inteiro: "))

soma = n1 + n2
sub1 = n1 - n2
sub2 = n2 - n1
multi = n1 * n2
div = n1 / n2
resto = n1 % n2

print(f"A soma entre os dois números informados é {soma}.")
print(f"A subtração do primeiro pelo segundo número é {sub1}.")
print(f"A subtração do segundo pelo primeiro número é {sub2}.")
print(f"A multiplicação entre os dois números é {multi}")
print(f"A divisão do primeiro pelo segundo número é {div}")
print(f"O resto da divisão entre o primeiro e o segundo número é {resto}.")