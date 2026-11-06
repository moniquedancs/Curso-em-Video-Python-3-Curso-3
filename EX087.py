#Aprimorando o desafio anterior, mostrando no final:
#A) Soma dos valores pares digitados
#B) Soma dos valores da terceira coluna
#C) Maior valor da segunda coluna

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares = 0
terceira = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]

maior_2_coluna = max(matriz[l][1] for l in range(3))

print("*" * 20)

for l in range(3):
    print("|", end=" ")
    for c in range(3):
        print(f"{matriz[l][c]:>3}", end=" ")
    print("|")

print(f"A) Soma dos valores pares: {soma_pares}")
print(f"B) Soma da terceira coluna: {terceira}")
print(f"C) Maior valor da segunda coluna: {maior_2_coluna}")



