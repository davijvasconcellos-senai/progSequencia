"""
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a apenas em dias.
Obs: Considere os anos 365 dias e os meses com 30 dias

Idade em anos: ?
meses se passaram desde seu último aniversário
dias se passaram após a contagem dos meses anterior
 resp: dias de vida
"""

idade_anos = int(input("Qual a sua idade? "))
meses = int(input("Quantos meses completos já se passaram desde o seu último aniversário? "))
dias = int(input("Quantos dias se passaram após a contagem dos meses anterior? "))

dias_vida = (idade_anos * 365) + (meses * 30) + dias

print(f"Você já viveu {dias_vida:.0f} dias.")