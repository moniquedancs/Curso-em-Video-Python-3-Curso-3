#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:

    n = int(input("Digite um número: "))
    lista.append(n)
    perg = str(input("Deseja continuar? [S/N] ")).upper().strip()
    if perg == "N":
        print("Encerrando...")
        break

for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f"Os números digitados foram: {sorted(lista)}.")
print(f"Os números pares foram: {sorted(par)}.")
print(f"Os números ímpares foram: {sorted(impar)}.")
