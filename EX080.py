#Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção. No final, mostre a lista ordenada na tela).

lista = []

for c in range (1,6):
    n = input(f"Digite o {c}º número: ")

#Se a lista estiver vazia, basta apenas adicionar o primeiro elemento.
    if len(lista) == 0:
        lista.append(n)

#Procurando a posição correta
    else:
        posicao = 0 #inicia na posição zero
        #Enquanto a posição for menor que a contagem de elementos na lista
        #E 0 for menor que n
        #posição soma mais 1
        while posicao < len(lista) and lista[posicao] < n:
            posicao += 1
        lista.insert(posicao, n) #coloca o elemento em uma posição específica
print(lista)
