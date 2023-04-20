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
def substitution_cle(alphabet):  # fonction qui permets de générer une clé de substitution aléatoire
    substitution_key=list(alphabet)  # crée une copie de la liste d'origine pour servir de clé de substitution
    random.shuffle(substitution_key)  # mélange la liste pour obtenir une clé aléatoire
    res = ""  # créé une chaîne vide pour stocker la clé de substitution
    for char in substitution_key:  # parcourt chaque caractère dans la clé de substitution
        res += char  # ajoute le caractère à la chaîne de résultat
    return res  # renvoie la clé de substitution sous forme de chaîne de caractères

key = substitution_cle(alphabet)
 

def encrypt(lignes, substitution_key):  # fonction qui permets de crypter le message d'origine
    encrypted_message = ""  # variable vide ou sera stocker le message crypté
    for char in lignes:  # on parcourt tout les caractères du message d'origine
        if char.lower() in alphabet:  # si le caractére fait partit de l'alphabet et si il est en minuscule
            index = alphabet.index(char.lower())  # récupère l'index du caractère dans la liste alphabet
            if char.isupper():   # si le caractére est en majuscule
                encrypted_message += substitution_key[index%len(substitution_key)].upper()  # ajoute la lettre de substitution correspondante en majuscule
            else:  # sinon, le caractère est en minuscule
                encrypted_message += substitution_key[index%len(substitution_key)]  # ajoute la lettre de substitution correspondante en minuscule
        else:  # si le caractère n'est pas alphabétique,
            encrypted_message += char  # ajoute le caractère original tel quel
    return encrypted_message  # renvoie le message chiffré


def decrypt(lignes, key):
    decrypted_message = ""  # initialise une chaîne vide pour stocker le message déchiffré
    for char in lignes:  # parcourt chaque caractère dans le message chiffré
        if char.lower() in key:  # vérifie si le caractère est alphabétique (en minuscule) et dans la clé
            index = key.index(char.lower())  # récupère l'index du caractère dans la clé de substitution
            if char.isupper():  # si le caractère est en majuscule,
                decrypted_message += alphabet[index].upper()  # ajoute la lettre d'origine correspondante en majuscule                                                  
            else:  # sinon, le caractère est en minuscule
                decrypted_message += alphabet[index]  # ajoute la lettre d'origine correspondante en minuscule
        else:  # si le caractère n'est pas alphabétique ou n'est pas dans la clé de substitution,
            decrypted_message += char  # ajoute le caractère original tel quel
    return decrypted_message  # renvoie le message déchiffré

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


# ---print substitution---
print("Message en clair :", messsage)

encrypted_message = encrypt(message, key)
print("Message chiffré :", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Message déchiffré :", decrypted_message)

print(cle)
# ----- 



