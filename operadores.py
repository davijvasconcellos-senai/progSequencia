a = 3
b = -4

# Operadores Aritméticos
soma = a + b
sub = a - b
mult = a * b
div = a / b
div_inteiros = a // b

print("Soma: ", soma)
print("Subtração: ", sub)
print("Multiplicação: ", mult)
print("Divisão: ", div)
print("Divisão de inteiros: ", div_inteiros)
print("Cálculos dentre de print: ", (a * b))
print("Resto da divisão de 11 por a: ", (11 % a))

# Operadores ralacionais
print("a == b:", (a == b))
print("a < 5:", (a < 5))
print("a > b:", (a > b))
print("a <= 3:", (a <= 3))
print("a >= 4:", (a >= 4))
print("a != b:", (a != b))

# Operadores Lógicos
logic1 = True
logic2 = False
print(type(logic1))
print(type(logic2))

print(logic1)
print(not logic1)
print(logic1 or logic2)
print(logic1 and logic2)