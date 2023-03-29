"Tableau des questions-R�ponses"

Questions=[["En quelle ann�e se sont d�roul�s les JOs de P�kin ?" , "Combien de sports sont repr�sent�s aux JOs ?" , "Qui a gagn� le tournoi de Wimbledon en 2014 ?"	, "Qui a gagn� la coupe de football de 1998 ?" , "Au basket, combien de point(s) rapporte(nt) un dunk ?"], 
           ["Quelle figure de style consiste �coller deux mots de sens contraires dans une phrase ?", "Quel grand dramaturge est l'auteur de la pi�ce 'Le Malade Imaginaire ?'", "Quel c�l�bre �crivain romantique du XVIIIe est à l'origine du receuil 'Les Contemplations' ?", "Dans quel registre figure l'expression de la piti� en litt�rature ?", "De quel mot fran�ais utilis� g�n�ralement durant la p�riode moyennageuse provient le terme chaussure ?"],
           ["Combien de pays sont membres de l'UE actuellement ?" , "Quelle est la capitale du Guatemala?"	, "De quel pays Jakarta est-elle la capitale ?", "Quel est le plus long fleuve fran�ais ?", "Combien y-a-t-il de continents (hors Antartique) ?"],
           ["En quelle ann�e s'est produit la tr�s c�l�bre bataille de Waterloo ?", "En quelle ann�e s'est produite la d�claration d'ind�pendance des Eu ?", "Quel grand empereur romain a vaincu Vercing�torix en 52 av. J-C ?", "Quel autre nom tr�s c�l�bre donne-t-on � la traite n�gri�re entre l'Europe, l'Afrique noire et l'Am�rique datant du XVIIIe si�cle ?" , "En quelle ann�e s'est d�roul�e la chute du mur de Berlin ?"]]

Reponses=[["2008", "33", "Djokovic", "France", "2"], ["oxymore", "Moli�re", "Hugo", "path�tique", "chausse"], ["27", "Guatemala", "Indon�sie", "Loire", "6"], ["1815", "1783", "Jules C�sar", "commerce triangulaire", "1989"]]



"Fonctions"

from random import randint

  
def partie(Questions, Reponses, questions_max):
    nb_bonnes_rep=0
    questions_posees=[]
    for question in range(questions_max):
        domaine=randint(0,3)
        num_question=randint(0,4)
        question_posee=Questions[domaine][num_question]
        if question_posee in questions_posees:
            domaine = randint(0,3)
            num_question=randint(0,4)
            question_posee=Questions[domaine][num_question]
        print(question_posee)
        questions_posees.append(question_posee)
        reponse=input()
        if str(reponse)==str(Reponses[domaine][num_question]) or str(Reponses[domaine][num_question]) in str(reponse):
            nb_bonnes_rep+=1
            print("Bonne R�ponse !")
        else:
            print("Mauvaise R�ponse !")
    print("Partie Termin�e !")
    print("Vous avez",nb_bonnes_rep,"bonnes réponses !")

partie(Questions, Reponses, 10)
