#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

perg = input("Digite uma expressão matemática: ")

contador = 0
valida = True

for caractere in perg:
    if caractere == "(":
        contador += 1
    elif caractere == ")":
        contador -= 1
    if contador < 0:
        valida = False
        break

if valida and contador == 0:
    print("Sua expressão está correta!")
else:
    print("Sua expressão está errada!")

