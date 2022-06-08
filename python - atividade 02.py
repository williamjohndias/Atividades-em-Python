#declaração de variáveis
x = 0
y = 1
lista = []

#enquanto 1 for igual a 0 faça..
while y == 1:
    #digitar um número inteiro e insere em x
    n = int(input('Digite um número: [ %s ]: ' % x))

    #se o número digitado for igual ou menor que 0 escreva..
    if n <= 0:
      print('valor erro')
      #para a aplicação
      break
    #senão
    else:
      #adiciona mais um item à lista e adiciona mais um valor a x
      lista.append(n)
      x += 1

#lista os números dentro da lista
print('Esses são os números que você digitou...', lista)
#operador de soma (sum), soma os itens da lista e armazena na variável "soma"
soma = sum(lista)
#junto do operador (len) para verificar quantos itens há na lista, utiliza-se a soma e divide pela quantidade de itens na lista
media = soma /len(lista)
#mostra a soma dos valores da lista retornando a variável "soma"
print('A soma dos valores são:', soma)
#mostra a media dos valores da lista retornando a variável "media"
print('A média dos valores são:', media)
#juntamente do operador (min) retorna o valor mínimo da lista (menor número)
print('O menor valor é:', min(lista))
#juntamente do operador (max) retorna o valor máximo da lista (maior número)
print('O maior valor é:', max(lista))
