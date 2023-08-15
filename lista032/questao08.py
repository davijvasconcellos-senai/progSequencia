"""
Fazer um algorítmo que receba o preço de custo de um produto e mostre como resposta o valor de venda.
Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usário
"""

custo = float(input("Informe o preço custo do produto: "))
percentual = float(input("Informe o percentual de acréscimo: "))

acrescimo = custo * percentual / 100

venda = custo + acrescimo

print("O valor de venda do produto é R$ {:.2f}".format(venda))