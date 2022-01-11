import csv
import os
import re

try:
    os.mkdir("inscrits_total")
except FileExistsError:
    pass


#reinitialise inscrits-total
f = open("inscrits_total/inscrits_total.csv", 'w')
f.close()

#trouver tous les fichiers voisins et les mets dans une liste
chemin = os.getcwd()
liste = (os.listdir(chemin))
print(liste)

#trouver dans liste les fichiers commencant par inscrit-20
for i in liste:
    if re.match("inscrits-20",i):
        print(i)
#ouvrir chaque fichier qui match et afficher chaque ligne
        with open(i,"r") as dossier:
            fichierliste = csv.reader(dossier, delimiter=";")
            for line in fichierliste:
                print(line)
# ouvrir fichier inscrit_total, afficher chaque ligne et comparer avec la ligne du fichier qui match /  si pareil, doublon =1
                doublon = 0
                csvfile = open("inscrits_total/inscrits_total.csv", "r")
                spamreader = csv.reader(csvfile, delimiter=";")
                for tuple_total in spamreader:
                    if tuple_total == line:
                        print("doublon-refuser")
                        doublon = 1
                csvfile.close()
# Si aucune ligne identique entre la totalité de inscrit_total et la ligne du fichier qui match, ajouter la ligne a inscrits-total
                if doublon != 1:
                    with open("inscrits_total/inscrits_total.csv", 'a', newline='') as csvfile:
                        spamwriter = csv.writer(csvfile, delimiter=';')
                        spamwriter.writerow(line)

Non_admis = 0
Poussin = 0
Cadet = 0
Junior = 0
Semi_pro = 0
Pro = 0

with open("inscrits_total/inscrits_total.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=";")
    for line in csvfile:
        csv_row = line.split()
        print(line[2])


