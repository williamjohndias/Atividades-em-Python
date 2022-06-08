x = 0

y = int(input("digite um número: "))

soma = 0

if( x % 2 != 0 ):
  x += 1
while( x <= y ):
  soma = soma + x
  x += 2
print( soma )
