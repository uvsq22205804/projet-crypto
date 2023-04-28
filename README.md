# Cryptanalyse de chiffrements
### Groupe : L1BI-TD02
Iliane IDRI--TURREL,
Emma CLUZET,
Sawsane EL AOUNI

## L'url de dépôt du projet

https://github.com/uvsq22205804/projet-crypto

## Utilisation du programme

Le programme doit crypter des messages en ayant une clé de chiffrement donnée. Plusieurs fonctions encryptage et décryptage différentes sont utilisées. 

Il y a donc 8 fonctions chiffrement et déchiffrement qui prennent en entrée une chaîne de caractères et la clef qui renvoie le chiffré. Ainsi que des fonctions qui prennent en entrée un chemin dans l'ordinateur contenant le chemin du fichier contenant un texte à chiffrer ou à déchiffrer.
De plus à partir d'un texte chiffré, sans connaissance de la clef, le programme doit retrouver une partie ou toute la clef et/ou le message inital.
Pour cela, il va falloir manipuler des chaînes de caractères, on veillera à laisser la possibilité à l’utilisateur de supprimer les espaces ou les caractères spéciaux, chiffrer un texte écrit dans un fichier .txt qui se situerait n’importe où dans l’ordinateur, ou généraliser le code de César ou le chiffre de Vigenère à des alphabets plus grands

Puis nous avons une fonction qui permet de retrouver le message crypté par les fonctions précédentes sans connaître la clé de déchiffrement. Il va donc tester toutes les possibilités et l'utilisateur pourra déterminer quel est le résultat le plus probant.


### Le code César

Le  code de cesar est issu d'un décallage de 3 lettres dans l'alphabet pour créer un clé de chiffrage. Ici le code traite d'abord les espace puis dans un second temps il recupere l'indice de la lettre pour la stocker dans une variable i en y ajoutant le decalage. Si ce dernier est superieur a 25, on calcul le reste de la division que l'on stocke dans "i". On ajoute a la variable texte_chiffre, la lettre avec son indice décalé.
Puis pour dechiffré le message choisi, le programme traite aussi dans un premier temps les espaces puis les lettre en cette fois si soustrayant le decalage. Encore une fois, si ce dernier est superieur a 25, on calcul le reste de la division que l'on stocke dans "i". On ajoute a la variable texte_chiffre, la lettre avec son indice décalé.


### Substitution monoalphabétique generale

Une substitution monoalphabétique est un cryptage issus d'une clé aléatoire unique. Dans notre cas nous avons donc dans un premier temps une fonction qui génère une clé aléatoire, en mélangeant, avec la methode "shuffle()" une liste copie de l'alphabet. Une fois la clé obtenue on peut commencer un coder un message. La fonction qui encrypte, va tout d'abord parcourir l'entièreté des caractéres du texte et voit si ils font parti de l'aphabet et si ils sont en majuscules ou en minuscules. Ensuite on récupère son indice afin de trouver sa substitution dans la clé et on le remplace. Si le caractère n'est pas alphabétique le code le met dans sa forme originale dans le nouveau texte. Pour le déchiffrement il faut faire la meme chose mais cette fois ci en prenant l'indice du caractère de la clé d'abord, pour ensuite trouvé quel caractère il substitue.


### Précisions
Iliane aillant des problèmes avec son vscode. Emma fait les commit + push à sa place.

