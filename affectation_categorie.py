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
    #Demande d'inscription nombre avec cas d'erreur
    while True:
        connaitre_nombre = input("Connaissez-vous le nombres de personnes a inscrire? Oui(1) / Non(2)\n")
        if connaitre_nombre == "1" or connaitre_nombre == "2":
            break
        else:
            print("Merci de répondre par le chiffre 1 ou le chiffre 2")

    if connaitre_nombre == "1":
        while True:
            try:
                nbr = int(input("Combien de demande d'inscription souhaitez vous faire?\n"))
                break
            except ValueError:
                print("Ce n'est pas un nombre valide, entrez un nombre sous forme de chiffres")
    if connaitre_nombre == "2":
        nbr = 0
    return nbr

def enrg_inscription_nbr_connu(nbr):

    liste_final = []
    for i in range(1, nbr + 1):
        print("-------", i, "inscription ------")
        a = input("insérer le nom\n")
        b = input("insérer le prénom\n")

        while True:
            try:
                c = int(input("insérer l'année de naissance\n"))
            except ValueError:
                print("Ce n'est pas un nombre valide, entrez un nombre sous forme de chiffres")
            if c >= 1900 and c < 2050:
                break
            else:
                print("entrez une date de naissance à partir de 1900.")

        liste_inscription = []
        liste_inscription.append([donnee_complete(a, b, c)[0]])
        liste_inscription.append([donnee_complete(a, b, c)[1]])
        liste_inscription.append([donnee_complete(a, b, c)[2]])
        liste_inscription.append([donnee_complete(a, b, c)[3]])
        print(liste_inscription)

        liste_final.append(liste_inscription)

    return liste_final

def enrg_inscription_nbr_inconnu(nbr):
    liste_final = []
    while True:
        while True:
            ajout_nv_personne = input("Voulez vous ajouter un nouvel enregistrement? Oui(1) / Non(2)\n")
            if ajout_nv_personne == "1" or ajout_nv_personne == "2":
                break
            else:
                print("Merci de répondre par le chiffre 1 ou le chiffre 2")

        if ajout_nv_personne == "1":
            nbr += 1
            print("-------", nbr, "inscription ------")
            a = input("insérer le nom\n")
            b = input("insérer le prénom\n")

            while True:
                try:
                    c = int(input("insérer l'année de naissance\n"))
                except ValueError:
                    print("Ce n'est pas un nombre valide, entrez un nombre sous forme de chiffres")
                if c >= 1900 and c < 2050:
                    break
                else:
                    print("entrez une date de naissance à partir de 1900.")

            liste_inscription = []
            liste_inscription.append([donnee_complete(a, b, c)[0]])
            liste_inscription.append([donnee_complete(a, b, c)[1]])
            liste_inscription.append([donnee_complete(a, b, c)[2]])
            liste_inscription.append([donnee_complete(a, b, c)[3]])
            print(liste_inscription)

            liste_final.append(liste_inscription)

        if ajout_nv_personne == "2":
            break
    return liste_final




def enregistrement_inscription():

    nbr = nbr_a_inscrire()
    if nbr >= 1:
        liste_final = enrg_inscription_nbr_connu(nbr)
    if nbr == 0:
        liste_final = enrg_inscription_nbr_inconnu(nbr)
    return liste_final



a = enregistrement_inscription()
print(a)

