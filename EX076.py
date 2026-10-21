#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

prod = ("Lápis", 1.00, "Borracha", 0.50, "Caneta", 1.50, "Marca-Texto", 2.50, "Caderno", 25.00)

print("----- TABELA DE PREÇOS -----")

#Buscando os produtos
for i in range (0,10,2):
    print(f"{prod[i]:.<20}R${prod[i+1]:>5.2f}")

#:.<20 = até 20 caracteres serão alinhados depois do nome do produto
#:.>5 = até 5 caracteres serão alinhados depois de R$