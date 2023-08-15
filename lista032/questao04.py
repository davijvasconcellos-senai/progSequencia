"""
Desenvolver um programa que pergunte ao usuário o seu peso e a sua altura. Ao final o programa
exibir na tela do índice de massa corporal desta pessoa (IMC)
"""
import math

peso = float(input("Informe o seu peso em quilos: "))
altura = float(input("Informe a sua altura em metros: "))

imc = peso / math.pow(altura,2)

print(f"De acordo com os dados informados, seu imc é {imc:.2f}.")