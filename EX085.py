#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []] #lista única

for c in range(1, 8):
    n = int(input(f"Digite o {c}º número: "))
    if n % 2 == 0:
        lista[0].append(n) #posição 0 é par
    else:
        lista[1].append(n) #posição 1 é ímpar

#Ordem crescente
lista[0].sort()
lista[1].sort()

print(f"Os números pares são: {lista[0]}")
print(f"Os números ímpares são: {lista[1]}")