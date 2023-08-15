"""
Fazer um algoritmo que pergunte 1 número e apresente:

A) O próprio número
B) O quadrado deste número
C) A raiz quadrada deste número
"""
import math

num = int(input("Por favor um informe um número inteiro: "))

quad = math.pow(num,2)
r_quad = math.sqrt(num)

print(f"O número que você informou é: {num}")
print(f"O quadrado deste número é: {quad}.")
print(f"A raiz quadrada deste número é: {r_quad}.")

# var "QUAD", é para calcular a potência do número informado.
# var "R-QUAD", é para calcular a raiz quadrada do número informado.