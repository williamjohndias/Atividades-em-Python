#variável(number), insere-se um valor inteiro 
number = int(input("Digite um valor: "))
#variável(a) recebe o valor da variável(number)
a = number
#gerador de matriz bidimensional aninhada
a = [[i + j for j in range(0, number+ 1)] for i in range(0, number+ 1)]
#mostra a matriz na tela
for row in a:
    ts = (" ".join([str(elem) for elem in row]))
    print(ts)
