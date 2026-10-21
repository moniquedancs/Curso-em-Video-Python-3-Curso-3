#Crie um programa que vai ler vários números e colocar em uma lista, e mostrar:
#Quantos números foram digitados:
#A lista de valores ordenados de forma decrescente:
#Se o valor 5 foi digitado e está na lista.

lista = []

while True:

    n = int(input("Digite um número: "))
    lista.append(n)
    perg = str(input("Deseja continuar? S/N")).upper().strip()

    if perg == "N":
        print("Encerrando...")
        break

print(f"A quantidade de números digitados foi de {len(lista)} números.")
print(f"Os números digitados, em ordem descrescente: {sorted(lista, reverse=True)}.")

if 5 in lista:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")