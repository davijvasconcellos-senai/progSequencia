valor1 = 8.79
valor2 = 3932.6
valor3 = 11.349

# Exibição simples do valor da variável.
print("Valor 3: {}".format(valor3))

# Exibição formatando como float
print("Valor 1: {:f}".format(valor1))

# Exibindo float com decimal em dois dígitos.
print("Valor 1: {:.2f}".format(valor1))
print("Valor 2: {:.2f}".format(valor2))
print("Valor 3: {:.2f}".format(valor3))

# Formatação float, com total de 7 dígitos(números e ponto), sendo 2 decimais.
print("Valor 1: {:7.2f}".format(valor1))
print("Valor 2: {:7.2f}".format(valor2))
print("Valor 3: {:7.2f}".format(valor3))

# Semelhante ao anterior, mas preenche com zeros à esquerda quando necessário
print("Valor 1: {:07.2f}".format(valor1))
print("Valor 2: {:07.2f}".format(valor2))
print("Valor 3: {:07.2f}".format(valor3))