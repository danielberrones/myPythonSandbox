import random,time
prep=['autor de ','au-delà de ','en face de ' ,
      "à l'intérieur de ",'devant ','dans ','proche de ', 'loin de ', "a l'extérieur de "]

nouns=['la forêt','la bibliotheque',"l'église",'la maison',
       'la fille','la banque','la boulangerie','la salle',
       'la poste','la serviette']

verbes=['dire','penser','croire','savoir','regarder','utiliser','nettoyer','lire','rendre','découvrir',
        'montrer','descendre','faire','mettre','courir',"choisir","trouver","laisser","arriver","sentir",
        "rester","appeler","perdre","jouer","rentrer","commencer","manger","aimer","frapper","donner","parler",
        "passer","voir"]
questions=["Qu'est-ce que tu en penses? ", "Pourquoi il a décidé de faire ça? ","Tu crois que c'est bon? ",
           "Tu aurais fait cela ?","Pourquoi a-t-elle fait cela? ", "Ferais-tu cela? ", "Que penses-tu? "]
sujet=['Je suis ','Tu es ','Il est ','Elle est ', "On est ","Nous sommes ","Vous êtes ","Ils sont ","Elles sont "]
while True:
    for x in prep:
        print(random.choice(sujet)+random.choice(prep)+random.choice(nouns)+" pour "+random.choice(verbes))
        time.sleep(1)
        print()
        print(random.choice(questions))
        input()
        print()
        
