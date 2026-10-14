#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num = ()
par = ()

print("Análise de Números")
print("-"*20)

for c in range(1,5):
    perg = int(input(f"Digite o {c}º número: "))
    num += (perg,)

print(f"Você digitou os números {num}.")

#Quantas vezes apareceu o número 9:
print(f"O número 9 aparece {num.count(9)} vezes.")

#Posição do número 3:
if 3 in num:
    print(f"O número 3 apareceu na {(num.index(3) + 1)}º posição.")
else:
    print("Não há número 3.")

#Números pares:
for m in num:
    if m % 2 == 0:
        par += (m,)

if par:
    print("Os números pares foram:", *par)
else:
    print("Não há números pares.")