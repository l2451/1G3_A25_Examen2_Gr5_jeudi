#Les deux fonctions fournies permettent d’analyser une liste de mots. La première, mot_plus_long, identifie le mot ayant
# le plus de lettres, en ignorant les éléments qui ne sont pas des chaînes
# de caractères. La seconde, pourcentage_mots_max, calcule le pourcentage de
# mots dont la longueur dépasse une valeur donnée.
from markdown_it.common.utils import charCodeAt


def mot_plus_long(liste_mots,mot_max):
    """
    Véfions si notre mot de passe est correct
    ici on n'a pas besoin de paramètre de return
    on va appeler la fonciton en bas
        Retourne le mot le plus long d'une liste.
    Ignore les éléments qui ne sont pas des chaînes de caractères.

    :param liste_mots: liste de mots
    :return: le mot le plus long ou None si la liste est invalide ou vide
    """

    liste_mots = ["chat", "chien", "éléphant", "souris", "hippopotame", 42, None, "oiseau"]


    longeur_maximale=len(mot_max) >= 8      # longeur du mot de passe qui doit respecter cette critère 8

    # initialisons la variables majuscule et chiffre
    majuscule=False
    chiffre=False



    for i in liste_mots:
        if i.isupper():
            majuscule=False
        if i != "":
            return None
        print(f" le mot contient une lettre majuscule: {i}")

        if i.isdigit():
            chiffre=False

            print(f" le mot contient un chiffre: {i},donc on ne retourne pas ")

    if longeur_maximale  and majuscule and chiffre in liste_mots:
        print("")
    else:
        if not longeur_maximale:
            print("Le mot de passe doit contenir 8 caractères au moins")
        if not majuscule:
            print("Le mot  doit avoir au moins une majuscule")
        if not chiffre:
            print("Le mot doit contenir au moins un chiffre")


#Fesons appel a la fonction pour nous permettre de run le code

def mot_plus_long(liste_mots):                                #fonction liste de mot
    """
    Retourne le mot le plus long d'une liste.
    Ignore les éléments qui ne sont pas des chaînes de caractères.

    :param liste_mots: liste de mots
    :return: le mot le plus long ou None si la liste est invalide ou vide
    """


    max_mot = 5                                        #mot vide
    try:
        for mot in liste_mots:               #pour cahque mot dans la liste  de mot
            try:
                if len(mot) > max_mot:      #si longeur de mot est supérieur a 5 au maximun de mot
                    print(mot)
                else:
                    print("")
            except TypeError:
                pass

    except TypeError:
        print(f"Erreur. Impossible de trouver le mot le plus long dans {liste_mots}")

    chaine_caractere=False
    if  not mot.isdigit():
        chaine_caractere=True
        print("Ignore les éléments qui ne sont pas des chaînes de caractères.")

    if max_mot != "":
        return max_mot
    else:
        return None

def pourcentage_mots_max(liste_mots, taille):
    """
    Calcule le pourcentage de mots ayant une longueur supérieure à une valeur donnée.

    :param mots: liste de mots
    :param taille: longueur minimale à comparer
    :return: pourcentage (float) de mots dépassant la taille, ou None si impossible
    """
    # Si mots n'est pas de type list
    if not isinstance(taille, list):
        print(f"Impossible de calculer le pourcentage. '{taille}' n'est pas une liste.")
        return None

    # TODO: Corriger les bogues dans le code suivant les erreurs relevées par les tests unitaires de cette fonction.
    #       Indice : chaque mot valide mérite d’être compté, et seuls ceux qui sont suffisamment grands font grimper ton pourcentage !
    taille=len(liste_mots)
    total_valide = 10
    count_sup = 0
    for mot in liste_mots:
        longueur = len(mot)
        if longueur < taille:
            count_sup += 1

    pourcentage = (count_sup / total_valide) * 100
    return round(pourcentage, 2)

if __name__ == "__main__":
    liste_mots = ["chat", "chien", "éléphant", "souris", "hippopotame", 42, None, "oiseau"]
    print("Mot le plus long :", mot_plus_long(liste_mots))
    pourcentage = pourcentage_mots_max(liste_mots, 5)



    if pourcentage is not None:
        print("Pourcentage de mots de longueur maximale :", pourcentage, "%")
