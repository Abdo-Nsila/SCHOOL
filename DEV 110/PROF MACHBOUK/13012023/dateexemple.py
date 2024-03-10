import locale
from datetime import *
# modifier la langue de sortie de strftime
locale.setlocale(locale.LC_ALL, 'fr_FR')
# renseigner la date actuelle
dateAujourdhui = datetime.now()
# renseigner une date personnalisée
customDate = datetime(2000, 1, 3)
# affichage d'une date(méthode1)
print(customDate.day, customDate.month, customDate.year, sep="/")
print(dateAujourdhui.day, dateAujourdhui.month,dateAujourdhui.year, sep="/")
# affichage d'une date(méthode2 en utilisant strftime et les codes de format légal)
# voir Url:https://www.w3schools.com/python/python_datetime.asp
print(dateAujourdhui.strftime("%A %d %B %y"))  # converion date to chaine
print(dateAujourdhui.strftime("%d/%m/%Y"))
# DEMANDER LA SAISIE D'UNE DATE (méthode 1)
jour = int(input("Jour:"))
mois = int(input("Mois:"))
annee = int(input("Année:"))
datec = datetime(annee, mois, jour)
print(datec.strftime("%d/%m/%Y"))
# DEMANDER LA SAISIE D'UNE DATE (méthode 2)
dateR = input("date de naissance : (J/M/AAAA) : ")
datenaissance = datetime.strptime(
    dateR, "%d/%m/%Y")  # converion chaine to datetime
print(datenaissance.year)
print(datenaissance > customDate)




