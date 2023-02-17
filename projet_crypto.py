# Emma : code de césar + scytale
# Sawsane : chiffre de vigenère 
# Iliane : une substitution monoalphabétique générale

# - - - - - - - - - - - - -
# Déclaration des fonctions
# - - - - - - - - - - - - -

""" Code de César   """
# alpha : alphabet

def chiffrement(alpha, texte, decalage):
    texte_chiffre = ""
    for i in texte:  # i : variable contenant l'indice de texte
        for j in range(len(alpha)):  # j : variable contenant l'indice de alpha
            if i== alpha[j]:
                
                texte_chiffre += alpha[j + decalage]
    
    return texte_chiffre

def dechiffrement(alpha, texte_chiffre, decalage):
    texte_dechiffre = ""
    for i in texte_chiffre:  # i : variable contenant l'indice de texte
        for j in range(len(alpha)):  # j : variable contenant l'indice de alpha
            if i == alpha[j]:
                texte_dechiffre += alpha[j - decalage]
    return texte_dechiffre


""" Chiffre de Vigenère """
# réutiliser fonction chiffrement du code de césar
# on utilise toujours le même déclage dans le tableau du chiffre de Vigenère 

"""Scytale"""

"""substitution monoalphabetique générale"""


# - - - - - - - - - -
# Programme principal
# - - - - - - - - - -

# une liste avec alphabet et on pourra choisir le décalage


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
mon_texte = "totoparapluie"
decalage = 3
# texte = input("Quel est votre message: ")
# decalage = int(input("Quel sera le décalage : "))
mon_texte.lower()  # met tout le texte en minuscule pour ne pas avoir de problème avec les majuscules
txt_chiffre = chiffrement(alphabet, mon_texte, decalage)
print(txt_chiffre)
txt_dechiffre = dechiffrement(alphabet, txt_chiffre, decalage)
print (txt_dechiffre)



