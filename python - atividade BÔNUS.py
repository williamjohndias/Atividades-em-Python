#mostra na tela
print("+====================+")
print("| INICIO DO PROGRAMA |")
print("+====================+")
#cria uma lista vazia
lista = []
#enquanto verdadeiro..
while True:
    #mostra na tela (MENU)
    print("+----------------+")
    print("| MENU PRINCIPAL |")
    print("+----------------+")
    print("| 1. incluir     |")
    print("| 2. excluir     |")
    print("| 3. listar      |")
    print("| 0. sair        |")
    print("+----------------+")
    #declara a variável(opcao) para se inserir um valor inteiro(int)
    opcao = int(input('Digite uma opção: '))

    #se a variável(opcao) for igual à 1 então..
    if opcao == 1:
	#mostra na tela
        print('Você decidiu inserir um valor :)')
	#declara a variável(inserir ) para se inserir um valor inteiro(int)
        inserir = int(input('digite um número: '))
	#mostra na tela o valor da variável(inserir)
        print('Valor inserido com sucesso!! :)', inserir)
	#ADICIONA um valor à lista (variável(lista))
        lista.append(inserir)
    #senão se a variável(opcao) for igual à 2 então..
    elif opcao == 2:
	#mostra na tela
        print('Você decidiu excluir um valor :)')
	#exclui o último valor da lista (variável(lista))
        lista.pop()
        print('número removido :(')
    #senão se a variável(opcao) for igual à 3 então..
    elif opcao == 3:
	#mostra na tela
        print('Você decidiu listar os valores :)')
	#mostra na tela a variável(lista) completa
        print(lista)
    #senão se a variável(opcao) for igual à 0 então..
    elif opcao == 0:
	#mostra na tela
        print('Fechando o programa...')	
	#finaliza a aplicação
        break
    #senão então..
    else:
	#mostra na tela
        print('Opção inválida!')

