import csv
import os
import re

f = open("inscrits_total.csv", 'w')
f.close()

chemin = os.getcwd()
liste = (os.listdir(chemin))

for i in liste:
    if re.match("inscrits-20",i):
        print(i)
        with open(i,"r") as dossier:
            for line in dossier:
                print(line)
                with open("inscrits_total.csv", 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=';')
                    spamwriter.writerow([line])









# def ecrire(fichier):
#     with open(fichier, 'w', newline='') as csvfile:
#         spamwriter = csv.writer(csvfile, delimiter=';')
#         for i in liste_final:
#             spamwriter.writerow(i)
#
# ecrire("inscrits_total.csv")