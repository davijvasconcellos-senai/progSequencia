"""
Fazer um algoritmo que pergunte o nome do vendedor, o seu salário fixo e o total de vendas efetuadas por ele no
mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, exibir ao final o seu
nome, e salário fixo, a comissão e o salário completo (fixo + comissão sobre as vendas) no final do mês.
"""

nome = (input("Informe o seu nome: "))
sal_f = float(input("Informe o seu salário fixo: "))
total_vendas = float(input("Iforme o total de vendas: "))

comissao = total_vendas * 15 /100
sal_completo = sal_f + comissao

print(f"Vendedor {nome}")
print("Salário fixo {:.2f}".format(sal_f))
print("Sua comissão é de R$ {:.2f}".format(comissao))
print("Seu salário completo é de R$ {:.2f}".format(sal_completo))