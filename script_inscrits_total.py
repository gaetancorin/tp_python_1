import csv
import os
import re

try:
    os.mkdir("inscrits_total")
except FileExistsError:
    pass



f = open("inscrits_total/inscrits_total.csv", 'w')
f.close()

chemin = os.getcwd()
liste = (os.listdir(chemin))
print(liste)

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









# def ecrire(fichier):
#     with open(fichier, 'w', newline='') as csvfile:
#         spamwriter = csv.writer(csvfile, delimiter=';')
#         for i in liste_final:
#             spamwriter.writerow(i)
#
# ecrire("inscrits_total.csv")