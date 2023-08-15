"""
Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit,
e apresente esta temperatura convertida em graus Celsius. A fórmula da conversão é

c = (f - 32) x 5 : 9
, onde c é a temperatura em graus Celsius e f en Fahrenheit.
"""

f = float(input("Informe uma temperatura em Graus Fahrenheit: "))

c = (f - 32) * 5 / 9

print(f, " graus Fahrenheit corresponde à {:.0f}".format(c), "Graus Celsius.")