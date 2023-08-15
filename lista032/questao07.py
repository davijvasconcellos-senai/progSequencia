'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que pergunte um
valor de uma compra, o númerode prestações escolhidas e apresente como resultado o valor das prestações.
'''

valor = float(input("Informe o valor à vista do produto desejado: "))
prestacao = float(input("Informe a quantidade de prestações desejadas (máximo 10): "))

valor_prestacao = valor / prestacao

print("Cada uma prestação será de R$ {:.2f}.".format(valor_prestacao))