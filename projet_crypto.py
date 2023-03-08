# Emma : code de césar + scytale
# Sawsane : chiffre de vigenère 
# Iliane : une substitution monoalphabétique générale

# - - - - - - - - - - - - -
# Déclaration des fonctions
# - - - - - - - - - - - - -

""" Code de César : """


def chiffrement_cesar(texte, key, alphabet):
    texte_chiffre = ''
    for lettre in texte:
        occurence = alphabet.find(lettre)  # stocke l'occurence des lettres dans le texte
        i = occurence + key  # i correspond à l'indice de la lettre chiffrée
        if i > 25:  # si i dépasse la taille de l'alphabet 
            i = i % 26  # on calcule le reste de la division et on la stocke dans i
        texte_chiffre += alphabet[i]  # on ajoute a la variable texte_chiffre la lettre avec l'indice décalé
    return texte_chiffre


def dechiffrement_cesar(texte, key, alphabet):
    texte_dechiffre = ''
    for lettre in texte:
        occurence = alphabet.find(lettre)  # stocke l'occurence des lettres dans le texte
        i = occurence - key  # i correspond à l'indice de la lettre chiffrée
        if i > 25:  # si i dépasse la taille de l'alphabet 
            i = i % 26  # on calcule le reste de la division et on la stocke dans i
        texte_dechiffre += alphabet[i]  # on ajoute a la variable texte_chiffre la lettre avec l'indice décalé
    return texte_dechiffre


""" Chiffre de Vigenère """
# réutiliser fonction chiffrement du code de césar
# on utilise toujours le même déclage dans le tableau du chiffre de Vigenère 

"""Scytale"""

"""substitution monoalphabetique générale"""


# - - - - - - - - - -
# Programme principal
# - - - - - - - - - -

# ----- Code de César -----

alphabet = "abcdefghijklmnopqrstuvwxyz"
message = input("Quel est votre message ? ")
cle = int(input("Quel est la clé de chiffrement de votre message? "))
message.lower()  # met tout le texte en minuscule pour ne pas avoir de problème avec les majuscules
message_chiffre = chiffrement_cesar(message, cle, alphabet)
print("Le message chiffré est :", message_chiffre)
message_dechiffre = dechiffrement_cesar(message_chiffre, cle, alphabet)
print("Le message déchiffré est:", message_dechiffre)

# ----- 



