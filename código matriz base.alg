algoritmo "matriz"
var
   mat: vetor[1..4,1..4] de inteiro
   i, j: inteiro
inicio
    // preenche a matriz
    // um laço dentro do outro para percorrer todas
    // as linhas e colunas da matriz
    para i de 1 ate 4 faca
        // a cada execução da variável i
        // a variável j começa de novo
        para j de 1 ate 4 faca
            mat[i,j] <- i + j
        fimpara
    fimpara
    
    escreval("Impressao da matriz")
    para i de 1 ate 4 faca
        para j de 1 ate 4 faca
            escreva(mat[i,j], " ")
        fimpara
        escreval()
    fimpara
    
    escreval()
    escreval("Imprime so a diagonal principal")
    para i de 1 ate 4 faca
        para j de 1 ate 4 faca
            se i = j entao
                escreva(mat[i,j]," ")
            senao
                escreva(". ")
            fimse
        fimpara
        escreval()
    fimpara
    
fimalgoritmo
