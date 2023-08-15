"""
Desenvolver um programa que faça duas peguntas: o valor referente às horas atuais e o valor referente aos
minutos atuais. Exemplo, se agora são 09:35, o usuário deverá informar como resposta às horas atuais o valor
09 e como resposta aos minutos o valor 35. Em seguida o programa deverá apresentar como resposta quantos minutos
já se passaram desde às 00:00h deste dia.
"""

hora = int(input("Por favor informe as horas: "))
min = int(input("Por favor informe os minutos: "))

total_min = (hora * 60) + min

print(f"Já se passaram {total_min} minutos desde a meia-noite.")