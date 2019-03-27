


#Faça um Programa que leia 5 números inteiros e os armazene em uma lista.
#Armazene os números pares na lista PAR e os números ÍMPARES na lista ı́mpar.
#Imprima as três listas. Utilize função para classificar os números.

import random

lista = []
par = []
impar = []

for i in range(5):
    digito = int ( input ( "Digite um número: " ) )
    lista.append(digito)

    if digito % 2 == 0:
        par.append(digito)

    else:
        impar.append(digito)

lista.sort()
par.sort()
impar.sort()

print ("\nLISTA = ", lista)
print ("PAR   = ", par)
print ("IMPAR = ", impar, "\n")