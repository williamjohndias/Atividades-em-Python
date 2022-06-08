
#declaração de variáveis que podem receber valores inteiros(int)
a1 = int(input('Primeiro termo: '))
a2 = int(input('Segundo termo: '))
a3 = int(input('Terceiro termo: '))
a4 = int(input('Quarto termo: '))

#declara as variáveis e nelas estão os valores para descobrir a "razão"
r1 = a2 - a1
r2 = a3 - a2
r3 = a4 - a3

#se as variáveis(r1, r2, r3) forem iguais então..
if r1 == r2 == r3:
    #mostra na tela
    print('É uma PA')
    #mostra a variável(r1), pois se são iguais não faz diferença qual delas mostrar
    print('a razão delas foi: ', r1)
#senão..
else:
    #mostra na tela
    print('Não é uma PA')
    #mostra as variáveis(r1, r2, r3), pois elas não são iguais, então será mostrado a razão do porque não são iguais
    print('a razão delas foi: ', r1, r2, r3)
#mostra na tela
print('-=-' * 11)

#tente.. (função para se o primeiro der erro, passará para o except)
try:
    #declara as variáveis e nelas estão os valores para descobrir a "razão"
    rpg1 = a2 / a1
    rpg2 = a3 / a2
    rpg3 = a4 / a3
    #se as variáveis(rpg1, rpg2, rpg3) forem iguais então..
    if rpg1 == rpg2 == rpg3:
	#mostra na tela
        print('É uma PG')
	#mostra a variável(rpg1), pois se são iguais não faz diferença qual delas mostrar
        print('a razão delas foi: ', rpg1)
    #senão..
    else:
	#mostra na tela
        print('Não é uma PG')
	#mostra as variáveis(rpg1, rpg2, rpg3), pois elas não são iguais, então será mostrado a razão do porque não são iguais
        print('A razão delas foi: ', rpg1, rpg2, rpg3)
#função para dizer que é impossível fazer uma divisão por 0
except ZeroDivisionError:
    #mostra na tela	
    print('Impossível ser uma PG')
#mostra na tela
print('-=-' * 11)
#mostra na tela quais foram os números inseridos nas variáveis(a1, a2, a3, a4)
print('a sequência é: {', a1,',', a2,',', a3,',', a4, '}')








