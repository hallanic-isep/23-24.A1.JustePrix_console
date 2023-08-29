# Tirage au sort d'un prix entre 1 et 10
import random
cible = random.randint(1,10)
essai = None

def verif(cible_param, essai_param):
    # Message "Bravo" si le prix est trouvé
    if cible_param == essai_param:
        print("Bravo !!!")
        return 0
    # Message "PAS ASSEZ" si le prix est trop bas
    elif cible_param > essai_param:
        print("Pas assez !!!")
    # Message "TROP ELEVE" si le prix est trop haut
    else:
        print("Trop elevé !!!")
    return 1

print(__name__)

if __name__ == '__main__':

    for i in range(1,6):
        # choix du prix du joueur
        try:
            essai = int(input(f"essai n°{i} - prix ? "))
        except:
            print("Valeur incorecte...")
            continue # Redémarre à l'itération suivante

        if verif(cible,essai) == 0:
            break

    # Message "PERDU" au bout de 5 essais
    if (cible != essai):
        print("Perdu...")

    # Fin au bout de 5 essais ou si le prix est trouvé
