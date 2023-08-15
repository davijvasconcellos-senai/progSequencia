"""
Fazer um programa que pergunte um valor em Dólares e apresente o equivalente em Reais.
Considere U$1,00 = R$ 3,80
"""

dolar = float(input("Informe um valor em dólares para ser convertido em reais: "))

real = dolar * 3.80

print("O valor informado convertido para a moeda brasileira é {:.2f}".format(real),".")