#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    leitura = int(input("Digite um número entre 0 e 20: "))

    if leitura >= 0 and leitura <= 20:
        escolha = n[leitura]
        break

    else:
        print("Número inválido. Tente novamente.")

print(f'Você escolheu o número {leitura}. Por extenso, escreve-se: {escolha}.')



