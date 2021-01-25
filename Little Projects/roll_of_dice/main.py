import random

print("Bienvenue au lancer de dé")

est_ce_que_il_veux_lancer_le_de = True

lancer_de = input("Appuyer sur entré pour lancer le dé")

while est_ce_que_il_veux_lancer_le_de:
    nombre_aleatoire_du_lancer = random.randrange(1, 6, 1)
    print("Lancer de dé : " + str(nombre_aleatoire_du_lancer))

    est_ce_que_il_veux_lancer_le_de = input("Est-ce que voulez-vous relancer le dé ?")


print("")
# l'utilisateur ne veux le dé
# ?