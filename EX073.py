#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Santos', 'Coritiba Red Bull', 'Bragantino', 'São Paulo', 'Botafogo', 'Vitória', 'Corinthians', 'Mirassol', 'Vasco', 'Grêmio', 'Internacional', 'Remo', 'Chapecoense')
titulo = 'CAMPEONATO BRASILEIRO DE FUTEBOL'
print("="*40)
print(f"{titulo:^40}")
print("="*40)

#cinco_times = (times [0:5])
#ultimos = (times[17:20])
#alfa = sorted(times)
#chapeco = times.index("Chapecoense")

print("Os 5 primeiros times são: ")
for pos, time1 in enumerate (times [0:5]):
    print(f'{pos+1}ª - {time1}')

print("="*40)

print("Os últimos 4 colocados são: ")
for pos, time2 in enumerate(times[16:20], start=17):
    print(f'{pos}ª - {time2}')

print("="*40)

print("Os times em ordem alfabética são:")
print(', '.join(sorted(times))) # "join" junta todos os nomes em um único texto

print("="*40)

print(f'O time da Chapecoense está na {times.index("Chapecoense")+1}ª posição.')


