# Code d'iliane fait avec ChatGPT

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

# Générer une clé de substitution aléatoire
substitution_key = list(alphabet)
random.shuffle(substitution_key)
substitution_key = "".join(substitution_key)

def encrypt(message, key):
    """
    Cette fonction prend un message en clair et une clé de substitution
    et retourne le message chiffré avec la substitution monoalphabétique.
    """
    encrypted_message = ""
    for char in message:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            if char.isupper():
                encrypted_message += key[index].upper()
            else:
                encrypted_message += key[index]
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, key):
    """
    Cette fonction prend un message chiffré avec une substitution monoalphabétique
    et la clé de substitution utilisée et retourne le message déchiffré en clair.
    """
    decrypted_message = ""
    for char in message:
        if char.lower() in key:
            index = key.index(char.lower())
            if char.isupper():
                decrypted_message += alphabet[index].upper()
            else:
                decrypted_message += alphabet[index]
        else:
            decrypted_message += char
    return decrypted_message

message = "Bonjour, comment ça va ?"
print("Message en clair :", message)

encrypted_message = encrypt(message, substitution_key)
print("Message chiffré :", encrypted_message)

decrypted_message = decrypt(encrypted_message, substitution_key)
print("Message déchiffré :", decrypted_message)