# Emma : code de césar + scytale
# Sawsane : chiffre de vigenère + une substitution monoalphabétique générale
""" Code de César """

def chiffrement(alpha, texte):
    for i in texte.items():  # i : variable contenant l'indice de texte
        for j in alpha.items():  # j : variable contenant l'indice de alpha
            if texte[i]==alpha[j]:
                texte_chiffre = alpha[j]
        pass

def dechiffrement():
    pass

# soit dictionnaire où on va aller chercher à quoi correspond chaque lettre, soit une liste avec tout
# l'alphabet et pour récupérer la bonne lettre on décale l'indice de 1
"""alphabet = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f":"i", "g": "j","h": "k", "i": "l",
            "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s","q": "t", "r": "u",
            "s": "v", "t": "w", "u": "x" ,"v": "y", "w": "z", "x": "a", "y": "b", "z":"c",}"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
mon_texte = "totoparapluie"
# texte = input("Quel est votre message: ")



""" Chiffre de Vigenère """