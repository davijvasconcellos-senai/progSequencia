"""
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará
em uma viagem. O programa deve coletar as seguintes informações: Distância a percorrer na
viagem, e, quilômetros; qual é o valor do consumo médio do automóvel, em quilômetros por litro.
"""

d = float(input("Informe a distância da viagem à ser percorrida em quilômetros: "))
c_m = float(input("Informe o consumo médio do seu veículo, em quilômetros: "))

litros = d / c_m

valor = litros * 5.00
print(f"Considerando a distância informada, e o consumo médio do seu veículo, você gastará {litros:.0f} litros de combustível, ")

print(f"e você gastará no total R$ {valor:.2f} para abastecer o seu veículo.")