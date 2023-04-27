# Emma : code de césar + scytale
# Sawsane : chiffre de vigenère 
# Iliane : une substitution monoalphabétique générale 

# - - - - - - - - - - -
# Import de librairies
# - - - - - - - - - - -

import tkinter as tk
import random
from os.path import isfile, realpath, dirname

# -------------------
# Création de fenêtre
# -------------------

root = tk.Tk()
root.title("Cryptanalyse de chiffrements")

cle = tk.Entry(root)
cle.grid(row= 1, column= 1)

label_cle = tk.Label(root, text= "Entrez votre clé de chiffrement (nombre)")
label_cle.grid(row= 1, column= 0)

message_chiffre = tk.Entry(root)
message_chiffre.grid(row= 4, column= 1)

label_message_chiffre = tk.Label(root, text= "Message chiffré")
label_message_chiffre.grid(row= 4, column= 0)

chargement = tk.Entry(root)
chargement.grid(row= 1,column= 1)

# - - - - - - - - - - - - -
# Déclaration des fonctions
# - - - - - - - - - - - - -


def charger_fichier(nom_du_fichier):
  mon_chemin = realpath(nom_du_fichier)  # récupère le chemin du fichier
  with open(mon_chemin,"r") as f:
    return f.readlines()
  

def sauvegarde(file_name, text= ''):
    if isfile(mon_chemin):
        mon_chemin = realpath(file_name)
    else :
        mon_chemin = realpath(__file__)
        mon_chemin = dirname(mon_chemin) + file_name
    file = open(file_name, "w")
    file.writelines(text)
    file.close()


""" Code de César : """


def chiffrement_cesar(texte, key, alphabet):
    texte_chiffre = ''
    for lettre in texte:
        if lettre == " ":
            texte_chiffre += " "
        else:
            occurence = alphabet.find(lettre)  # stocke l'occurence des lettres dans le texte
            i = occurence + key  # i correspond à l'indice de la lettre chiffrée
            if i > 25:  # si i dépasse la taille de l'alphabet 
                i = i % 26  # on calcule le reste de la division et on la stocke dans i
            texte_chiffre += alphabet[i]  # on ajoute a la variable texte_chiffre la lettre avec l'indice décalé
    return texte_chiffre


def dechiffrement_cesar(texte, key, alphabet):
    texte_dechiffre = ''
    for lettre in texte:
        if lettre == " ":
            texte_dechiffre += " "
        else:
            occurence = alphabet.find(lettre)  # stocke l'occurence des lettres dans le texte
            i = occurence - key  # i correspond à l'indice de la lettre chiffrée
            if i > 25:  # si i dépasse la taille de l'alphabet 
                i = i % 26  # on calcule le reste de la division et on la stocke dans i
            texte_dechiffre += alphabet[i]  # on ajoute a la variable texte_chiffre la lettre avec l'indice décalé
    return texte_dechiffre


""" Chiffre de Vigenère """
# réutiliser fonction chiffrement du code de césar
# on utilise toujours le même déclage dans le tableau du chiffre de Vigenère 


def chiffrement_vigenere(message, cle, alphabet, supprimer_espaces=True):
    if supprimer_espaces:
        message = ''.join(message.split()) # Supprime les espaces dans le message

    # Créer le tableau de substitution
    tableau = []
    for i in range(len(alphabet)):
        tableau.append([])
        for j in range(len(alphabet)):
            position = (j + i) % len(alphabet)
            tableau[i].append(alphabet[position])

    # Initialiser le texte chiffré
    chiffre = ""

    # Chiffrer le message
    for i in range(len(message)):
        lettre_message = message[i]
        position_lettre = alphabet.index(lettre_message.upper())
        lettre_cle = cle[i % len(cle)]
        position_cle = alphabet.index(lettre_cle.upper())
        chiffre += tableau[position_cle][position_lettre]

    return chiffre

def dechiffrement_vigenere(chiffre, key, alphabet, supprimer_espaces=True):
    if supprimer_espaces:
        chiffre = ''.join(chiffre.split()) # Supprime les espaces dans le message chiffré

    # Créer le tableau de substitution
    tableau = []
    for i in range(len(alphabet)):
        tableau.append([])
        for j in range(len(alphabet)):
            position = (j + i) % len(alphabet)
            tableau[i].append(alphabet[position])

    # Initialiser le texte déchiffré
    message = ""

    # Déchiffrer le message
    for i in range(len(chiffre)):
        lettre_chiffre = chiffre[i]
        position_cle = alphabet.index(cle[i % len(key)].upper())
        for j in range(len(alphabet)):
            if tableau[position_cle][j] == lettre_chiffre.upper():
                message += alphabet[j]

    return message


"""Scytale"""

"""substitution monoalphabetique générale"""


def substitution_cle(alphabet):  # fonction qui permets de générer une clé de substitution aléatoire
    substitution_key=list(alphabet)  # crée une copie de la liste d'origine pour servir de clé de substitution
    random.shuffle(substitution_key)  # mélange la liste pour obtenir une clé aléatoire
    res = ""  # créé une chaîne vide pour stocker la clé de substitution
    for char in substitution_key:  # parcourt chaque caractère dans la clé de substitution
        res += char  # ajoute le caractère à la chaîne de résultat
    return res  # renvoie la clé de substitution sous forme de chaîne de caractères


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


def decrypt(lignes, clef):
    decrypted_message = ""  # initialise une chaîne vide pour stocker le message déchiffré
    for char in lignes:  # parcourt chaque caractère dans le message chiffré
        if char.lower() in clef:  # vérifie si le caractère est alphabétique (en minuscule) et dans la clé
            index = clef.index(char.lower())  # récupère l'index du caractère dans la clé de substitution
            if char.isupper():  # si le caractère est en majuscule,
                decrypted_message += alphabet[index].upper()  # ajoute la lettre d'origine correspondante en majuscule                                                  
            else:  # sinon, le caractère est en minuscule
                decrypted_message += alphabet[index]  # ajoute la lettre d'origine correspondante en minuscule
        else:  # si le caractère n'est pas alphabétique ou n'est pas dans la clé de substitution,
            decrypted_message += char  # ajoute le caractère original tel quel
    return decrypted_message  # renvoie le message déchiffré

# - - - - - - -
# Cryptanalyse
# - - - - - - -


def casser_cesar(texte_dechiffre):
    """
    Cette fonction prend en entrée un texte chiffré avec le chiffrement César et retourne le texte déchiffré.
    La fonction effectue une attaque par force brute en testant toutes les clés possibles.
    """
    dechiffré = ""  # initialise une chaîne vide pour stocker le texte déchiffré
    for key in range(len(alphabet)):  # parcourt toutes les clés possibles (26 clés pour le chiffrement César)
        for c in texte_dechiffre:  # parcourt chaque caractère du texte chiffré
            if c.isalpha():  # vérifie si le caractère est alphabétique
                déchiffré += chr((ord(c) - ord('A') - key) % 26 + ord('A'))  # déchiffre le caractère en utilisant la clé courante
            else:  # si le caractère n'est pas alphabétique
                déchiffré += c  # ajoute le caractère tel quel au texte déchiffré
        print(f"Clé {key}: {dechiffré}")  # affiche le texte déchiffré pour la clé courante
        déchiffré = ""  # réinitialise le texte déchiffré pour la prochaine clé


# - - - - - - - - - -
# Programme principal
# - - - - - - - - - -

# ----- Code de César -----

alphabet = "abcdefghijklmnopqrstuvwxyz"

# ----- Substitution -----


clef = substitution_cle(alphabet)

# ----- Scytale -----



# ----- Vigenère -----




# -----------------------
# Boutons de chiffrements
# -----------------------

chiffre_cesar = tk.Button(root, text= "Chiffrement César", command= chiffrement_cesar(chargement,cle,alphabet))
chiffre_cesar.grid(row= 2, column=0)
dechiffre_cesar = tk.Button(root, text= "Déchiffrement César", command= dechiffrement_cesar)
dechiffre_cesar.grid(row= 3, column= 0)

c_vigenere = tk.Button(root, text="Vigenère", command= chiffrement_vigenere)
c_vigenere.grid(row= 2, column= 1)
d_vigenere = tk.Button(root, text= "Déchiffrement Vigenère", command= dechiffrement_vigenere)
d_vigenere.grid(row= 3, column= 1)

charge = tk.Button(root, text="Charger un fichier", command= charger_fichier(chargement))
charge.grid(row= 0, column= 0)



root.mainloop()
