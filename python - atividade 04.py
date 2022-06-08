#enquanto verdadeiro(True)
while True:
    #declara a variável(number), onde insere-se um valor inteiro
    number = int(input("Insira um número aqui: "))

    #limite    
    limit = number // 2
    #insere-se o valor definido como 0 na variável(total)
    total = 0
	
    #se number for diferente ou igual a 0 e number for diferente ou igual a 1 então..
    if number != 0 and number != 1:
	#valor da variável(total) recebe 1
        total = 1
    #se numver for divisível por 2 igual a 0 então..
    if number % 2 == 0:
	#insere na variável(total), a variável(limit) mais 2
        total += limit + 2

    #para cada item dentro de um limite de 3 até a variável(limit)
    for i in range(3, limit):
	#se a variável(number) for divisivel pelo item igual a 0 então..
        if number % i == 0:
	    #a variável(total) recebe +1 em seu valor
            total += i

    #verificar
    #se a variável(number) for igual a variável(total) então..
    if number == total:
	#mostra na tela:
        print("é perfeito")
    #se a variável(number) for igual a 0 então..
    elif number == 0:
	#mostra na tela:
        print('saindo..')
	#sai do loop, saindo da aplicação
        break
    else:
	#mostra na tela:
        print('não é perfeito')
