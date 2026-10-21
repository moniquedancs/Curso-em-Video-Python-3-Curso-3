#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:

    n = int(input("Digite um número: "))

    if n in lista:
        print("Valor duplicado, não será adicionado.")
    else:
        lista.append(n)
        print("Valor adicionado com sucesso!")

    perg = input("Deseja continuar? S/N ").upper().strip()
    if perg == "N":
        break

print(f"Os números adicionados foram {lista}.")
print(f"Em ordem crescente: {sorted(lista)}")