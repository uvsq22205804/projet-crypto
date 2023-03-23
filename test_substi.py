import string

def codage_substitution(subst, chaine, decode=False):
    """Crypte la chaîne en utilisant la substitution "subst".
La chaîne est convertie en majuscule d'abord, et seul l'ascii est traité.
La substitution est donnée par la liste des lettres substituées. Par exemple,
pour un décalage de 3 lettres, il suffit de donner la substitution
'DEFGHIJKLMNOPQRSTUVWXYZABC'. """
    alphabet = string.ascii_uppercase	# liste de toutes les lettres ASCII en majuscules
    chaine = chaine.upper()
    resultat = ""
    for c in chaine:
        n = alphabet.find(c)  	# on cherche l'indice de l'occurrence de c dans l'alphabet
        if n < 0:   			# si le caractère c n'est pas dans l'alphabet
            resultat = resultat + c 	# on le laisse tels quel
        else:       # si le caractère c est dans l'alphabet, on le remplace
            resultat = resultat + subst[n] # par le caractère qui a la même place dans la substitution 
    return resultat

chaine = "jnerijqgsoenfoekefn"
code = codage_substitution('DEFGHIJKLMNOPQRSTUVWXYZABC', chaine)
print("blabla")