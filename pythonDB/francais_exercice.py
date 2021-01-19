___author___="Daniel Alexander Berrones"

import random

verbes=['dire','penser','croire','savoir','regarder','utiliser','nettoyer','lire','rendre','découvrir',
        'montrer','descendre','faire','mettre','courir',"choisir","trouver","laisser","arriver","sentir",
        "rester","appeler","perdre","jouer","rentrer","commencer","manger","aimer","frapper","donner","parler",
        "passer","voir",'toucher','oublier','pouvoir','se sentir',"s'en dormir","envoyer","vivre","allumer"]
i=1
while True:
	a=random.choice(verbes)
	b= a.upper()
	print()
	print()	
	print(f"#{i}")
	questions="\nQu'est-ce que " + b + " veut dire?"
	print(questions)
	print("Alors, dis-moi! ")
	input(">  ")
	i += 1