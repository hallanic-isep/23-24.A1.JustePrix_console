# Tirage au sort d'un prix entre 1 et 10
import random
cible = random.randint(1,10)
essai = None

for i in range(1,6):
    # choix du prix du joueur
    try:
        essai = int(input(f"essai n°{i} - prix ? "))
    except:
        print("Valeur incorecte...")
        continue # Redémarre à l'itération suivante

    # Message "Bravo" si le prix est trouvé
    if cible == essai:
        print("Bravo !!!")
        break
    # Message "PAS ASSEZ" si le prix est trop bas
    elif cible > essai:
        print("Pas assez !!!")
    # Message "TROP ELEVE" si le prix est trop haut
    else:
        print("Trop elevé !!!")

# Message "PERDU" au bout de 5 essais
if (cible != essai):
    print("Perdu...")

# Fin au bout de 5 essais ou si le prix est trouvé
