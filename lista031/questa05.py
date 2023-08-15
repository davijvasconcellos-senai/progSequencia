"""
Fazer um programa que pergunte o salário de um funcionário e apresente este salário
com um aumento de 15%.
"""

sal = float(input("Informe o seu salário: ")) # var "SAL", é para o salário do funcionário.

add = sal * 15 / 100 # var "ADD", é para calcular o aumento de 15%.

sal_f = sal + add

print("Somando o seu salário com os acréscimos de 15%, você está recebendo: R$ {:.3f}".format(sal_f))

# var "SAR_F", é o resultado da soma do salário do funcionário + o acréscimo de 15%.