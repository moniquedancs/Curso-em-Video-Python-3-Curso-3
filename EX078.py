#Faça um programa que leia 5 valores e guarde-os em uma lista. No final, mostre qual foi o maior e o menor, e suas respectivas posições.

lista = []

for c in range (0,5):
    num = int(input(f"Digite um valor para a posição {c}: "))
    lista.append(num)

print(f"Os números digitados foram: {lista}.")
print(f"O maior número foi {max(lista)}, e está na posição {lista.index(max(lista))}.")
print(f"E o menor número foi {min(lista)}, e está na posição {lista.index(min(lista))}.")




