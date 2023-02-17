# Emma : code de césar + scytale
# Sawsane : chiffre de vigenère 
# Iliane : une substitution monoalphabétique générale

# - - - - - - - - - - - - -
# Déclaration des fonctions
# - - - - - - - - - - - - -

""" Code de César """
# alpha : alphabet

def chiffrement(alpha, texte, decalage):
    for i in texte:  # i : variable contenant l'indice de texte
        for j in alpha:  # j : variable contenant l'indice de alpha
            if texte[i]==alpha[j]:
                texte_chiffre = alpha[j + decalage]
    return texte_chiffre

def dechiffrement(alpha, texte, decalage):
    for i in texte:  # i : variable contenant l'indice de texte
        for j in alpha:  # j : variable contenant l'indice de alpha
            if texte[i]==alpha[j]:
                texte_dechiffre = alpha[j - decalage]

    return texte_dechiffre


""" Chiffre de Vigenère """
# réutiliser fonction chiffrement du code de césar
# on utilise toujours le même déclage dans le tableau du chiffre de Vigenère 


# - - - - - - - - - -
# Programme principal
# - - - - - - - - - -

# soit dictionnaire où on va aller chercher à quoi correspond chaque lettre, soit une liste avec tout
# l'alphabet et pour récupérer la bonne lettre on décale l'indice de 1
"""alphabet = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f":"i", "g": "j","h": "k", "i": "l",
            "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s","q": "t", "r": "u",
            "s": "v", "t": "w", "u": "x" ,"v": "y", "w": "z", "x": "a", "y": "b", "z":"c",}"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
mon_texte = "totoparapluie"
decalage = 3
# texte = input("Quel est votre message: ")
# decalage = int(input("Quel sera le décalage : "))
mon_texte.lower()  # met tout le texte en minuscule pour ne pas avoir de problème avec les majuscules
print(chiffrement(alphabet, mon_texte))
print("finish")


