Algoritmo "semnome"
Var
   op, i, num: inteiro
   vet: vetor[1..5] de inteiro
   posicaoatual: inteiro

Inicio
    posicaoatual <- 1
    escreval()
    escreval("+====================+")
    escreval("| INICIO DO PROGRAMA |")
    escreval("+====================+")

    repita
        escreval()
        escreval()
        escreval("+----------------+")
        escreval("| MENU PRINCIPAL |")
        escreval("+----------------+")
        escreval("| 1. incluir     |")
        escreval("| 2. excluir     |")
        escreval("| 3. listar      |")
        escreval("| 0. sair        |")
        escreval("+----------------+")

        escreva("Digite uma opcao: ")
        leia(op)
        escreval()
        escreval("Valor Digitado: ", op)
        escreval()
        escreval()

        escolha op
            caso 1
                 escreval("+----------+")
                 escreval("| INCLUSAO |")
                 escreval("+----------+")
                 se posicaoatual > 5 entao
                     escreval("Vetor cheio!! :(")
                 senao
                     escreval("Digite um numero: ")
                     leia(num)
                     se posicaoatual <= 10 entao
                         vet[posicaoatual] <- num
                         posicaoatual <- posicaoatual + 1
                         escreval("Inclusao realizada com sucesso!! :)")
                     fimse
                 fimse
            caso 2
                 escreval("+----------+")
                 escreval("| EXCLUSAO |")
                 escreval("+----------+")
                 se posicaoatual > 1 entao
                    posicaoatual <- posicaoatual - 1
                    escreval("Excluindo o valor ", vet[posicaoatual])
                    escreval("Exclusao realizada com sucesso!! :)")
                    vet[posicaoatual] <- 0
                 senao
                     escreval("Vetor Vazio!! :(")
                 fimse

            caso 3
                 escreval("+----------+")
                 escreval("| LISTAGEM |")
                 escreval("+----------+")
                 se posicaoatual = 1 entao
                     escreval("Vetor Vazio!! :(")
                 fimse
                 para i de 1 até posicaoatual-1 faca
                     escreva(vet[i], " ")
                 fimpara
            caso 0
                 escreval()
            outrocaso
                 escreval("-- Opcao invalida :( --")
        fimescolha
    até op = 0
    
    escreval("+====================+")
    escreval("|  FIM DO PROGRAMA   |")
    escreval("+====================+")
Fimalgoritmo

