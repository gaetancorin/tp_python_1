def categorie_age(age):
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

#a = int(input("inserer age\n"))

#b = categorie_age(a)
#print(b)