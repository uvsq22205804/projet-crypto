import string

def chiffrement(texte, decalage, alphabet):
    def decalage_alphabet(alphabet):
        return alphabet[decalage:] + alphabet[:decalage]  # [:]
    decalage_alphabet = tuple(map(decalage_alphabet, alphabet))  # map :transforme tous les éléments d'un itérable sans utiliser de boucle for
    final_alphabet = "".join(alphabet)  #
    final_decalage_alphabet = "".join(decalage_alphabet)
    table = str.maketrans(final_alphabet, final_decalage_alphabet)  # 
    return texte.translate(table)


mon_texte = "totoparapluie"
mon_texte.lower()
decalage = 3
chiffrement=chiffrement(mon_texte, decalage, [string.ascii_lowercase])
print(chiffrement)
"""
dechiffrement=chiffrement(chiffrement, decalage, [string.ascii_lowercase])
print(chiffrement)"""