#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#Quantas pessoas foram cadastradas;
#Uma listagem com as pessoas mais pesadas:
#Uma listagem com as pessoas mais leves.

geral = []
maispeso = []
menospeso = []

while True:
    nome = input("Digite o primeiro nome: ").strip()
    peso = float(input("Digite o peso (kg): ").replace(",", "."))
    geral.append([nome, peso])

    while True:
        perg = input("Deseja continuar? [S/N] ").strip().upper()
        if perg in ("S", "N"):
            break
        print("Erro, tente novamente.")
    if perg == "N":
        break

#p[0]: nome
#p[1]: peso

maior = max(p[1] for p in geral) #máximo valor de peso
menor = min(p[1] for p in geral) #mínimo valor de peso

for p in geral:
    if p[1] == maior: #se peso maior
        maispeso.append(p[0]) #nome da pessoa com peso maior
    if p[1] == menor: #se peso menor
        menospeso.append(p[0]) #nome da pessoa com peso menor

print(f"Quantidade de cadastros: {len(geral)} pessoas.")
print(f"Maior peso: {maior} kg, de: {maispeso}")
print(f"Menor peso: {menor} kg, de: {menospeso}")


