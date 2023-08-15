'''
Escreva um algoritimo que pergunte o número total de eleitores de um município, o número de votos brancos, nulos e
válidos e
apresente como respostao percentual que cada um representa em relação ao total de eleitores.

Total de eleitores de um município: ? ex: 1000
número de votos brancos ex: 100
número de votos de nulos ex: 200

resposta: números de votos de válidos
resposta: % votos brancos
resposta: % de votos nulos
resposta: % de votos válidos
'''

total_eleitores = float(input("Informe o total de eleitores do município: "))
votos_brancos = float(input("Informe o total de votos brancos: "))
votos_nulos = float(input("Informe o total de votos nulos: "))

votos_validos = total_eleitores - votos_brancos - votos_nulos

print("Total de votos válidos: {:.0f}".format(votos_validos))

perc_votos_brancos = (votos_brancos * 100) / total_eleitores
perc_votos_nulos = (votos_nulos * 100) / total_eleitores
perc_votos_validos = (votos_validos * 100) / total_eleitores

print("Percentual de votos em branco: {:.1f}%".format(perc_votos_brancos))
print("Percentual de votos nulos: {:.1f}%".format(perc_votos_nulos))
print("Percentual de votos válidos: {:.1f}%".format(perc_votos_validos))