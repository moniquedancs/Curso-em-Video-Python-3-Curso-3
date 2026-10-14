#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

lista = ( )
maior = menor = 0
from random import randint

for c in range (0,5):
    num = randint(1, 20)
    lista += (num,) #sem a vírgula, é apenas um número com parênteses.

    if c == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"Os números escolhidos são: {lista}.")
print(f"O menor é {menor} e o maior é {maior}.")






