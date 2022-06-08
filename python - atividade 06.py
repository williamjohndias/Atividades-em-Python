#declara as variáveis
totaleleitor = int(input("Total de eleitores do município: "))
votosvalidos = int(input("Total de votos válidos: "))
votosbrancos = int(input("Total de votos brancos: "))
votosnulos = int(input("Total de votos nulos: "))

#declara as variáveis com valores definidos (cálculo para saber a porcentagem % dos valores acima divididos pela variável(totaleleitor))
brancos = 100 * votosbrancos / totaleleitor
nulos = 100 * votosnulos / totaleleitor
validos = 100 * votosvalidos / totaleleitor

#mostra na tela
print("-="*20)
#mostra na tela o resultado dos cálculos..
print("Porcentagem de votos válidos é: ", validos, "%")
print("Porcentagem de brancos válidos é: ", brancos, "%")
print("Porcentagem de nulos válidos é: ", nulos, "%")
#mostra na tela
print("-="*20)
