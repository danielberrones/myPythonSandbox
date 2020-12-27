verbes=['dire','penser','croire','savoir','regarder','utiliser','nettoyer','lire','rendre','découvrir',
        'montrer','descendre','faire','mettre','courir',"choisir","trouver","laisser","arriver","sentir",
        "rester","appeler","perdre","jouer","rentrer","commencer","manger","aimer","tenir","donner","parler",
        "passer","voir"]
des_phrases=["Il va ","Nous voulons ", "Vous devez ","Elle veut ","Je vais ","Ils vont ","Tu veux ",
             "On peut ","Nous pouvons ", "Je peux ", "Tu vas ", "Elle peut ","J'ai besoin de ","Nous avons besoin de ",
             "Tu as besoin de ","Il te faut ", "Je souhaite ","Tu auras besoin de ","J'aurai besoin de ",
             "Nous allions ","Elles peuvent ","Il vous faudra ","Il allait ","Il devait "]

import random
from time import sleep

while True:
    for whatever in verbes:
        print(random.choice(des_phrases)+random.choice(verbes))
        sleep(1)

