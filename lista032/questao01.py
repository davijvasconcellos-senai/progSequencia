'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o valor
com o acréscimo dos 10% do garçom
'''

conta = float(input("Informe o valor da conta: "))

acrescimo = conta * 10/100
v_final = conta + acrescimo

print("O valor final da conta, somado com o acréscimo de 10% é de R$ {:.2f}.".format(v_final))