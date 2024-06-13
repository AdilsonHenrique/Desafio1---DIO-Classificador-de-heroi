nome_heroi = input(("Heroi qual é o seu nome?\n"))
xp = float(input("Quanto de XP o seu heroi tem?\n"))

if xp <= 1000:
    nivel = "ferro"
elif 1001 <= xp <= 2000:
    nivel = "bronze"
elif 2001 <= xp <= 5000:
    nivel = "prata"
elif 5001 <= xp <= 6000:
    nivel = "ouro"
elif 6001 <= xp <= 7000:
    nivel = "platina"
elif 7001 <= xp <= 8000:
    nivel = "ascendente"
elif 8001 <= xp <= 9000:
    nivel = "imortal"
else:
    nivel = "radiante"

print(f"Ola heroi {nome_heroi} verifique o seu nivel e atualmente você é {nivel}")