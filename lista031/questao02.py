"""
Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
A) Resultado de suas adições;
B) Resultado de suas multiplicações
"""

num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe um segundo número: "))
num3 = int(input("Informe um terceiro número: "))
num4 = int(input("Informe um quarto número: "))

add = num1 + num2 + num3 + num4 # var "ADD", é para realizar a operação de soma.
mult = num1 * num2 * num3 * num4 # var "MULT", é para realaizar a operação de multiplicação.

print(f"A soma destes números é {add} e a multiplicação é {mult}.")