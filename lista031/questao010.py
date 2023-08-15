"""
Fazer um algorítimo que efetue o cálculo do valor de uma prestação em atraso, utlilizando a fórmula:
prestação = valor + (valor x (taxa:1000 x tempo em dias).

Perguntar ao usuário:
 - valor da prestação
 - taxa de juros
 - tempo em dias

 Resposta:
 - Valor da prestação em atraso
"""

valor = float(input("Informe o valor normal da prestação: "))
taxa = float(input("Informe o valor da taxa de juros: "))
tempo = float(input("Informe quantos dias de atraso: "))

prestacao = valor + (valor * (taxa / 100)) * tempo

print("O valor da prestação em atraso é de  R$ {:.2f} ".format(prestacao),".")