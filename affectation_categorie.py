# Classe la personne en fonction de son année de naissance
def categorie_age(annee):
    age = 2022 - int(annee)
    if age < 6 or age > 40:
        return "Non admis"
    elif age < 12:
        return "Poussin"
    elif age < 18:
        return "Cadet"
    elif age < 24:
        return "Junior"
    elif age < 30:
        return "Semi-pro"
    elif age <= 40:
        return "Pro"

#a = int(input("inserer annee\n"))
#b = categorie_age(a)
#print(b)

# Créer son adresse email
def adresse_email(nom,prenom):
    a = str(prenom[0]+"."+nom+"@baton-rouge.fr")
    return a

#adresse_email("corin","gaetan")

def donnee_complete(nom,prenom, annee_naissance):
    adressemail = adresse_email(nom, prenom)
    categorie= categorie_age(annee_naissance)
    return nom, prenom, adressemail, categorie

def nbr_a_inscrire():
    nbr = int(input("Combien de demande d'inscription souhaitez vous faire?\n"))
    liste_inscrits = []
    for i in range(1, nbr+1):
        print("-------",i,"inscription ------")
        a = input("insérer le nom\n")
        b = input("insérer le prénom\n")
        c = input("insérer l'année de naissance\n")

        liste_inscription = []
        liste_inscription.append([donnee_complete(a, b, c)[0]])
        liste_inscription.append([donnee_complete(a, b, c)[1]])
        liste_inscription.append([donnee_complete(a, b, c)[2]])

        liste_inscrits.append(liste_inscription)

    #     print(liste_inscription)
    # print(liste_inscrits)
    return liste_inscrits


a = nbr_a_inscrire()
print(a)

