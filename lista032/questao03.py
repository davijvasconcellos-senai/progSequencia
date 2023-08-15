"""
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final
o programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros
"""

altura_m = float(input("Informe a sua altura em metros: "))
peso_kg = float(input("Informe o seu peso em quilos: "))

altura_cm = altura_m * 100
peso_g = peso_kg * 1000

print(f"Sua altura em centímetros é {altura_cm} , e seu peso em gramas é {peso_g}.")