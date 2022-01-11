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

#trouver dans liste les fichiers commencant par inscrit-20, ouvrir et pour chaque ligne, ecrire dans inscrit-total
for i in liste:
    if re.match("inscrits-20",i):
        print(i)
        with open(i,"r") as dossier:
            spamreader = csv.reader(dossier, delimiter=";")
            for line in spamreader:
                print(line)
                with open("inscrits_total/inscrits_total.csv", 'a') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=';')
                    spamwriter.writerow([line[0], line[1], line[2], line[3]])

