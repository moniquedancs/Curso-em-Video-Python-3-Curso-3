#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("casa", "carro", "janela", "porta")
vogais = ("a", "e", "i", "o", "u")

for v in range(0, len(palavras)):
    for l in range(0, len(vogais)):
        qtd = palavras[v].count(vogais[l])
        if qtd > 0:
            print(f"{palavras[v]}: {vogais[l]} aparece {qtd} vez(es)")